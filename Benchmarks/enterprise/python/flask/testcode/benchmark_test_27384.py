# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest27384():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = normalise_input(json_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return Markup('<img src="' + str(data) + '">')
    return jsonify({"result": "success"})
