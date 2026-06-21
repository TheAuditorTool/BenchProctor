# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os


def BenchmarkTest01848():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    return Markup('<img src="' + str(data) + '">')
