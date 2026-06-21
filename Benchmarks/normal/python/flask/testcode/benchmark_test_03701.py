# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest03701():
    xml_value = request.get_data(as_text=True)
    random.seed(int(xml_value) if str(xml_value).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
