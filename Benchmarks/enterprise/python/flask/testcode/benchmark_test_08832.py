# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest08832():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = normalise_input(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
