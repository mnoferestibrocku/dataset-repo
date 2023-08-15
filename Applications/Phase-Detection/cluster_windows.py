from minisom import MiniSom
from sklearn.cluster import KMeans 
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics
import numpy as np
import os
RANDOM_SEED = 200028



def kmeans_clustering_silhouette(dataset, min=10, max=20):
    best_silhouette = -1
    best_cluster = -1
    best_cluster_labels = []
    for x in range(min, max+1):
        if len(dataset) <= x:
           labels = [0]*len(dataset)
        else:
            kmeans = KMeans(n_clusters=x).fit(dataset)
            labels = kmeans.labels_
        if len(list(set(labels))) == 1:
           score = 0
        else:
            score = metrics.silhouette_score(dataset, labels)
        if score > best_silhouette:
           best_silhouette = score
           best_cluster = x
           best_cluster_labels = labels
    return list(best_cluster_labels)

def hierarch_clustering_silhouette(dataset, min=10, max=20):
    best_silhouette = -1
    best_cluster = -1
    best_cluster_labels = []
    for x in range(min, max+1):
        if len(dataset) <= x:
           labels = [0]*len(dataset)
        else:
            labels = AgglomerativeClustering(n_clusters=x, affinity='euclidean', linkage='ward').fit_predict(dataset)
        if len(list(set(labels))) == 1:
           score = 0
        else:
            score = metrics.silhouette_score(dataset, labels)
        if score > best_silhouette:
           best_silhouette = score
           best_cluster = x
           best_cluster_labels = labels
    return list(best_cluster_labels)

def kmeans_clustering(dataset, clusters = 20):
    if len(dataset) <= clusters:
        labels = [0]*len(dataset)
    else:
        kmeans = KMeans(n_clusters=clusters).fit(dataset)
        labels = kmeans.labels_
    return list(labels)

def hierarch_clustering(dataset, clusters = 20):
    if len(dataset) <= clusters:
        labels = [0]*len(dataset)
    else:
        labels = AgglomerativeClustering(n_clusters=clusters, affinity='euclidean', linkage='ward').fit_predict(dataset)
    return list(labels)

def som_clustering(dataset, r=10, c=10):
  data = np.array(dataset)
  som_shape = (r, c)
  first_stage_som = MiniSom(som_shape[0], som_shape[1], data.shape[1], sigma=.5, learning_rate=.5,
                neighborhood_function='gaussian', topology = 'hexagonal', random_seed=RANDOM_SEED)
  first_stage_som.train_batch(data, 500, verbose=True)

  winner_coordinates = np.array([first_stage_som.winner(x) for x in data]).T
  cluster_index = np.ravel_multi_index(winner_coordinates, som_shape)
  cluster_index = filter_labels(cluster_index)
  return cluster_index

def filter_labels(labels):
  new_labels = []
  keep_labels = []
  keep_labels = sorted(set(labels))
  for x in range(len(labels)):
    if labels[x] in keep_labels:
        new_labels.append(keep_labels.index(labels[x]))
    else:
      new_labels.append(-1)

  return new_labels

def save_labels(labels, vectors, outpath):
    log_outpath = outpath.split("/")
    log_outpath[-1] = "clusterlog_" + log_outpath[-1]
    log_outpath = "/".join(log_outpath)
    cluster_log = open(log_outpath+".txt", 'w')
    for x in range(len(list(set(labels)))):
      cluster_log.write("Cluster %d: %d (%0.3f percent)\n" %(x, labels.count(x), 100*labels.count(x)/len(labels)))
    cluster_log.close()

    output = open(outpath + "_labels.txt", 'w')
    for x in range(len(labels)):
        output.write(str(labels[x]) + ":" + ",".join([str(v) for v in vectors[x]]))
        if x != len(labels) - 1:
            output.write("\n")
    output.close()

"""
    SOM_clustering: whether or not to perform SOM clustering
    same_KMeans: whether or not to perform k-means clustering, using the same number of clusters as SOM (SOM_clustering must be true)
    same_hierarical: ^ with hierarchical clustering
    optimalKMeans: whether or not to perform k-means clustering, checking clusters from 10-20 and picking best silhouette score
    optimal_hierarchical: ^ with hierarchical clustering
    set_KMeans: perform KMeans with a predtermined number (eg 20), not performed if None
    set_hierarchical: ^ with hierarchical clustering
"""
def perform_clustering(vectors, outpath, 
                       SOM_clustering=True, 
                       same_KMeans = False, optimal_KMeans=True, 
                       same_hierarhical = False, optimal_hierarchical=True):
    if SOM_clustering:
        som_labels = som_clustering(vectors)
        save_labels(som_labels, vectors, outpath+"_som")
        clusters = len(list(set(som_labels)))
        if same_KMeans:
            try:
                kmeans_same_labels = kmeans_clustering(vectors, clusters)
                save_labels(kmeans_same_labels, vectors, outpath+"_samekmeans")
            except:
                print("Unable to kmeans cluster")
        if same_hierarhical:
            try: 
                hier_same_labels = kmeans_clustering(vectors, clusters)
                save_labels(hier_same_labels, vectors, outpath+"_samehierarch")
            except:
                print("Unable to hierarch cluster")
    if optimal_KMeans:
        try:
            opt_kmeans_labels = kmeans_clustering_silhouette(vectors)
            save_labels(opt_kmeans_labels, vectors, outpath+"_kmeans")
        except:
            print("Unable to kmeans cluster")
    if optimal_hierarchical:
        try:
            opt_hier_labels = hierarch_clustering_silhouette(vectors)
            save_labels(opt_hier_labels, vectors, outpath+"_hierarch")
        except:
            print("Unabel to hierach cluster")


def second_stage(mod_vectors, first_stage_labels, cluster_method):
    num_clusters = len(list(set(first_stage_labels)))

    vectors = [[] for x in range(num_clusters)]
    for x in range(len(first_stage_labels)):
        y = mod_vectors[x]
        z = first_stage_labels[x]
        vectors[z].append(y)

    sub_cluster_labels = []
    for v in vectors:
        l = cluster_method(mod_vectors)
        sub_cluster_labels.append(l)
    
    num_sub_clusters = []
    for x in range( len(sub_cluster_labels)):
        s = sub_cluster_labels[x]
        num_sub_clusters.append(len(list(set(s))))
    
    final_labels = []
    trackers = [0]*len(sub_cluster_labels)

    for x in range(len(first_stage_labels)):
        l = first_stage_labels[x]
        local_label = sub_cluster_labels[l][trackers[l]]
        trackers[l] += 1
        for y in range(l):
            local_label += num_sub_clusters[y]
        final_labels.append(local_label)
    return filter_labels(final_labels)


def perform_twostageclustering(vectors, mod_vectors, outpath, 
                       SOM_clustering=True, 
                       KMeans=True, 
                       hierarchical=True):
    if SOM_clustering:
        som_labels = som_clustering(vectors)
        labels = second_stage(mod_vectors, som_labels, som_clustering)
        save_labels(labels, vectors, outpath+"_som")
    if KMeans:
        try:
            opt_kmeans_labels = kmeans_clustering_silhouette(vectors)
            labels = second_stage(mod_vectors, opt_kmeans_labels, kmeans_clustering_silhouette)
            save_labels(labels, vectors, outpath+"_kmeans")
        except:
            print("unable to kmeans cluster")
    if hierarchical:
        try:
            opt_hier_labels = hierarch_clustering_silhouette(vectors)
            labels = second_stage(mod_vectors, opt_hier_labels, hierarch_clustering_silhouette)
            save_labels(labels, vectors, outpath+"_hierarch")
        except:
            print("unable to hierarch cluster")

