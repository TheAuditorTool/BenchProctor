# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify
from app_runtime import db


def BenchmarkTest01645():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
