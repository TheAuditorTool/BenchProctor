# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest63523():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
