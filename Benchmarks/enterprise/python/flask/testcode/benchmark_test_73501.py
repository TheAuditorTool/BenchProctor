# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from lxml import etree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest73501(path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
