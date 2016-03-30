from bson import json_util
import datetime
import falcon
import db_config
from settings import (
    MONGO_DB,
    DATABASE
)


class Links(object):

    def on_get(sef, request, response):
        client = db_config.get_client(MONGO_DB)
        db = db_config.get_database(client, DATABASE)
        links = db.links
        body = {}
        for link in links.find():
            body[unicode(link['_id'])] = link
        response.data = json_util.dumps(body)
        response.status = falcon.HTTP_200

    def on_post(self, request, response):
        raw_json = json_util.loads(request.stream.read())
        raw_json['date'] = datetime.datetime.now()
        client = db_config.get_client(MONGO_DB)
        db = db_config.get_database(client, DATABASE)
        links = db.links
        link_id = links.insert_one(raw_json).inserted_id
        response.data = json_util.dumps(
            {"details": "Link created with ID" + unicode(link_id)}
        )
        response.status = falcon.HTTP_200
