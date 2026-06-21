# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import os


def BenchmarkTest77115():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
