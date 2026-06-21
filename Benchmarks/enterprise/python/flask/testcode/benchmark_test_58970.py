# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


request_state: dict[str, str] = {}

def BenchmarkTest58970():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
