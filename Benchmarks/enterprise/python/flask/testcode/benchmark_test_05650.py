# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
from lxml import etree


def BenchmarkTest05650(path_param):
    path_value = path_param
    data = unquote(path_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
