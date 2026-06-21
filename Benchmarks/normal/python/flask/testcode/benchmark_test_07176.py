# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify
import os
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest07176():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return jsonify({"result": "success"})
