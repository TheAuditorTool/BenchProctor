# SPDX-License-Identifier: Apache-2.0
import json
from flask import Flask, request, jsonify
import importlib


def _revive_typed(fields):
    type_name = fields.pop('__type__', None)
    if type_name is None:
        return fields
    module_name, _, class_name = type_name.rpartition('.')
    return getattr(importlib.import_module(module_name), class_name)(**fields)

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00006", methods=["POST"])
def BenchmarkTest00006():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(data))
    return jsonify({'parsed': str(parsed)}), 200
