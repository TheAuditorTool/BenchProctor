# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest27096():
    secret_value = 'default_config_label'
    reader = make_reader(secret_value)
    data = reader()
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
