# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest03840():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    reader = make_reader(secret_value)
    data = reader()
    auth_check('user', data)
    return jsonify({"result": "success"})
