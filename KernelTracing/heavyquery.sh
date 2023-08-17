#!/bin/bash

while true; do

curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
    "size": 0,
    "aggs": {
      "top_ips": {
        "terms": {
          "field": "ip_src_host",
          "size": 5
        }
      }
    }
  }'

curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
    "size": 0,
    "aggs": {
      "top_source_ports": {
        "terms": {
          "field": "tcp_srcport",
          "size": 5
        }
      },
      "top_destination_ports": {
        "terms": {
          "field": "tcp_dstport",
          "size": 10
        }
      }
    }
 }'


curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
    "query": {
      "match": {
        "attacktype": "dns"
      }
    },
    "size": 5
  }'
  
curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
    "size": 0,
    "aggs": {
      "top_ips": {
        "terms": {
          "field": "Attack_type",
          "size": 10
        }
      }
    }
  }'

  
curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
    "query": {
      "range": {
        "dns_retransmit_request": {
          "gte": 0
        }
      }
    },
    "size": 0
  }'
 
curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
   "size": 0,
   "aggs": {
     "top_ips": {
       "terms": {
         "field": "tcp_ack_raw",
         "size": 5
       }
     }
   }
 }'

 
curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
    "size": 0,
    "aggs": {
      "attack_type_count": {
        "terms": {
          "field": "Attack_type",
          "size": 5,
          "order": {
            "_count": "asc"
          }
        }
      }
    }
 }'
 
curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
   "size": 0,
   "aggs": {
     "top_ips": {
       "terms": {
         "field": "tcp_dstport",
         "size": 5
       }
     }
   }
 }'

curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
    "query": {
      "bool": {
        "must_not": {
          "term": {
            "mqtt_protoname": "0"
          }
        }
      }
    },
    "size": 5
  }'
  

curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
    "size": 0,
    "aggs": {
      "top_tcp_documents": {
        "top_hits": {
          "size": 5,
          "sort": [
            {
              "tcp_len": {
                "order": "desc"
              }
            }
          ]
        }
      }
    }
  }'

sleep 40
done

