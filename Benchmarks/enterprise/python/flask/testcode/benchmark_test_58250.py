# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import os


def BenchmarkTest58250():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
