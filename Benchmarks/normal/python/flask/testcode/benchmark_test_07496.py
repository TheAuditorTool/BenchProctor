# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest07496(path_param):
    path_value = path_param
    data = unquote(path_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
