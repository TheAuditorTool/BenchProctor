# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49119():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    int(str(data))
    return jsonify({"result": "success"})
