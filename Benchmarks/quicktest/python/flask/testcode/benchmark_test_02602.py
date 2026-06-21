# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from lxml import etree


def BenchmarkTest02602(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
