# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07400():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    os.remove(str(data))
    return jsonify({"result": "success"})
