# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14519():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    os.seteuid(65534)
    return jsonify({"result": "success"})
