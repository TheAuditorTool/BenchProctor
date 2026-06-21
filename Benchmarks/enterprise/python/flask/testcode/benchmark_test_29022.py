# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest29022():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = normalise_input(forwarded_ip)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
