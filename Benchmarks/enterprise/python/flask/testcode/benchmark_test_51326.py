# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import pickle


def BenchmarkTest51326():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
