# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest04639():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = coalesce_blank(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
