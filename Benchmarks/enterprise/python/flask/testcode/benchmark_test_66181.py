# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify
import os
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest66181():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
