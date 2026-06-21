# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest47795():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
