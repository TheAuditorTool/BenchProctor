# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os


def BenchmarkTest01441():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    return Markup('<div>' + str(data) + '</div>')
