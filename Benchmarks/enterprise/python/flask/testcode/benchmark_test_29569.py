# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest29569(path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
