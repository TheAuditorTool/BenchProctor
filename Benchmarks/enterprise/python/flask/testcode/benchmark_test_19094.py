# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest19094():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
