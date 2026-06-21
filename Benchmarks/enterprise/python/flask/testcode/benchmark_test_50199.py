# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from lxml import etree
from app_runtime import db


def BenchmarkTest50199():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
