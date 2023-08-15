from elasticsearch import Elasticsearch
import csv

# Connect to Elasticsearch
es = Elasticsearch(['https://localhost:9200'],    verify_certs=False,http_auth=('elastic', 'elastic'))

# Define the index and document type
index_name = 'dnniodataset'
#doc_type = 'your_doc_type'

# Open the CSV file
with open('DNN-EdgeIIoT-dataset.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Prepare bulk indexing requests
    id = 1000
    bulk_data = []
    for row in reader:
        # Create your Elasticsearch document from the CSV row
        # Customize this based on your CSV structure and Elasticsearch mapping
        id = id +1
        # Example: Index a document with 'id' as the document ID
        source =  {
                'frame_time': row['frame.time'],
                'ip_src_host': row['ip.src_host'],
                'ip_dst_host': row['ip.dst_host'],
                'arp_dst_proto_ipv4': row['arp.dst.proto_ipv4'],
                'arp_opcode': row['arp.opcode'],
                'arp_hw_size': row['arp.hw.size'],
                'arp_src_proto_ipv4': row['arp.src.proto_ipv4'],
                'icmp_checksum': row['icmp.checksum'],
                'icmp_seq_le': row['icmp.seq_le'],
                'icmp_transmit_timestamp': row['icmp.transmit_timestamp'],
                'icmp_unused': row['icmp.unused'],
                'http_file_data': row['http.file_data'],
                'http_content_length': row['http.content_length'],
                'http_request_uri_query': row['http.request.uri.query'],
                'http_request_method': row['http.request.method'],
                'http_referer': row['http.referer'],
                'http_request_full_uri': row['http.request.full_uri'],
                'http_request_version': row['http.request.version'],
                'http_response': row['http.response'],
                'http_tls_port': row['http.tls_port'],
                'tcp_ack': row['tcp.ack'],
                'tcp_ack_raw': row['tcp.ack_raw'],
                'tcp_checksum': row['tcp.checksum'],
                'tcp_connection_fin': row['tcp.connection.fin'],
                'tcp_connection_rst': row['tcp.connection.rst'],
                'tcp_connection_syn': row['tcp.connection.syn'],
                'tcp_connection_synack': row['tcp.connection.synack'],
                'tcp_dstport': row['tcp.dstport'],
                'tcp_flags': row['tcp.flags'],
                'tcp_flags_ack': row['tcp.flags.ack'],
                'tcp_len': row['tcp.len'],
                'tcp_options': row['tcp.options'],
                'tcp_payload': row['tcp.payload'],
                'tcp_seq': row['tcp.seq'],
                'tcp_srcport': row['tcp.srcport'],
                'udp_port': row['udp.port'],
                'udp_stream': row['udp.stream'],
                'udp_time_delta': row['udp.time_delta'],
                'dns_qry_name': row['dns.qry.name'],
                'dns_qry_name_len': row['dns.qry.name.len'],
                'dns_qry_qu': row['dns.qry.qu'],
                'dns_qry_type': row['dns.qry.type'],
                'dns_retransmission': row['dns.retransmission'],
                'dns_retransmit_request': row['dns.retransmit_request'],
                'dns_retransmit_request_in': row['dns.retransmit_request_in'],
                'mqtt_conack.flags': row['mqtt.conack.flags'],
                'mqtt_conflag.cleansess': row['mqtt.conflag.cleansess'],
                'mqtt_conflags': row['mqtt.conflags'],
                'mqtt_hdrflags': row['mqtt.hdrflags'],
                'mqtt_len': row['mqtt.len'],
                'mqtt_msg_decoded_as': row['mqtt.msg_decoded_as'],
                'mqtt_msg': row['mqtt.msg'],
                'mqtt_msgtype': row['mqtt.msgtype'],
                'mqtt_proto_len': row['mqtt.proto_len'],
                'mqtt_protoname': row['mqtt.protoname'],
                'mqtt_topic': row['mqtt.topic'],
                'mqtt_topic_len': row['mqtt.topic_len'],
                'mqtt_ver': row['mqtt.ver'],
                'mbtcp_len': row['mbtcp.len'],
                'mbtcp_trans_id': row['mbtcp.trans_id'],
                'mbtcp_unit_id': row['mbtcp.unit_id'],
                'Attack_label': row['Attack_label'],
                'Attack_type': row['Attack_type'],
                # Add more fields as needed
        }
        document = {
            "index": {
                "_index": index_name,
            }
        }
        bulk_data.append(document)
        bulk_data.append(source)
        #print(document)
        #es.index(index="dnniodataset", body=document)
        # Add the document to the bulk indexing requests
        # Send bulk indexing requests in batches of 1000 documents
        if len(bulk_data) >= 10000:
            es.bulk(index=index_name, body=bulk_data)
            bulk_data = []
    
    # Send any remaining bulk indexing requests
    if len(bulk_data) > 0:
        es.bulk(index=index_name, body=bulk_data)

# Refresh the index to make the documents searchable
es.indices.refresh(index=index_name)

