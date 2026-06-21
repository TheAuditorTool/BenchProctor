# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest69942():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    reader = make_reader(prop_value)
    data = reader()
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
