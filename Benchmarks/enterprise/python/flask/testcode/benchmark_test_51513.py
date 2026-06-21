# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest51513():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
