# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from lxml import etree


def BenchmarkTest10284(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
