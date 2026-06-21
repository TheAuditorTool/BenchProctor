# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import jsonify
from types import SimpleNamespace
from app_runtime import redis_client


def BenchmarkTest53130():
    redis_value = redis_client.get('user_data')
    ns = SimpleNamespace(payload=redis_value)
    data = getattr(ns, 'payload')
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    requests.get(str(data))
    return jsonify({"result": "success"})
