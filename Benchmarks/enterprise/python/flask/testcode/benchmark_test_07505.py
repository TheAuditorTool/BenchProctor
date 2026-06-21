# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def BenchmarkTest07505():
    raw_body = request.get_data(as_text=True)
    if re.search('[a-zA-Z0-9_-]+', str(raw_body)):
        return jsonify({'validated': str(raw_body)}), 200
    return jsonify({"result": "success"})
