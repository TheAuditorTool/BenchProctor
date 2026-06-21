# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify
import time


def normalise_input(value):
    return value.strip()

def BenchmarkTest20448(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
