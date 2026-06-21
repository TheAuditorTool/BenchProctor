# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest74109():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
