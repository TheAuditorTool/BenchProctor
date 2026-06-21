# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest14716():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
