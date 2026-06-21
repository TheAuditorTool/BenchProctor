# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest59696():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
