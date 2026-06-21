# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from lxml import etree
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest56325():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ensure_str(db_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
