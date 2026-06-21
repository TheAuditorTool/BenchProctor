# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify
from app_runtime import db


def BenchmarkTest30925():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(comment_value) + '"]')
    return jsonify({"result": "success"})
