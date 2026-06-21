# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13617():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
