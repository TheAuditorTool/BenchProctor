# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest35777():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    os.remove(str(data))
    return jsonify({"result": "success"})
