# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest77983():
    field_value = request.form.get('field', '')
    data = coalesce_blank(field_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return render_template_string(data)
    return jsonify({"result": "success"})
