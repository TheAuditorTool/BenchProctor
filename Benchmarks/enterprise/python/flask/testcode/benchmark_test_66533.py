# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
from lxml import etree


@dataclass
class FormData:
    payload: str

def BenchmarkTest66533():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
