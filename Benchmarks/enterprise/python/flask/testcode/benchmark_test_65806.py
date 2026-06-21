# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from lxml import etree


@dataclass
class FormData:
    payload: str

def BenchmarkTest65806(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
