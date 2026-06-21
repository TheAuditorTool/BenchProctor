# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest45181():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = coalesce_blank(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
