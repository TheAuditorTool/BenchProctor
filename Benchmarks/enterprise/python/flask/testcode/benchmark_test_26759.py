# SPDX-License-Identifier: Apache-2.0
import os
from flask import redirect
import urllib.parse


def BenchmarkTest26759():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
