# SPDX-License-Identifier: Apache-2.0
import keyring
from flask import jsonify
from app_runtime import db


def BenchmarkTest04125():
    secret_value = 'feature_flag_value'
    pending = list(str(secret_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return jsonify({"result": "success"})
