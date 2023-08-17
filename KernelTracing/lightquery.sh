#!/bin/bash

while true; do

curl -k -u elastic:elastic -X POST "https://localhost:9200/dnniodataset/_search" -H "Content-Type: application/json" -d '{
    "size": 0,
    "aggs": {
      "top_source_ports": {
        "terms": {
          "field": "tcp_srcport",
          "size": 15
        }
      },
      "top_destination_ports": {
        "terms": {
          "field": "tcp_dstport",
          "size": 15
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
  
sleep 20
done

