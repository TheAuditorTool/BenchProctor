# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest00265():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
