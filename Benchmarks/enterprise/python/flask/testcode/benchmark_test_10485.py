# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest10485():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
