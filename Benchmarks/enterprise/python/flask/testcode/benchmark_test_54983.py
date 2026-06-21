# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest54983():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
