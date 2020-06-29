import xml.sax
import json
from doc import Doc
from doc_handler import DocHandler
from elasticsearch import Elasticsearch

if __name__=="__main__":
	es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	handler = DocHandler(es)
	parser.setContentHandler( handler )
	parser.parse("enwiki-20200620-abstract.xml")
