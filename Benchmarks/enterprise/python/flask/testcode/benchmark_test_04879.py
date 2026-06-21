# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest04879():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
