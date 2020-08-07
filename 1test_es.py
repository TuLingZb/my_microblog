import time

from elasticsearch.exceptions import TransportError
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

es.index(index='dasd1',id=12,body={'21':'wqew'},doc_type='doc')
# try:
response = es.search(index="test-index", body={"query": {"match_all": {}}})
# except TransportError as e:
#     time.sleep(5)
#     es = Elasticsearch()