# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from lxml import etree


def BenchmarkTest21849(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
