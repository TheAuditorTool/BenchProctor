# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os


def BenchmarkTest02401():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    return Markup('<div>' + str(data) + '</div>')
