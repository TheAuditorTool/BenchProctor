# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest20542():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
