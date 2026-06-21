# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify
from app_runtime import db


def BenchmarkTest26811():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
