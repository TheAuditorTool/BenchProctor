# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest43630():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
