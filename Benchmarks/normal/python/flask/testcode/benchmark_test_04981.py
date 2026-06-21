# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os


def BenchmarkTest04981():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    return Markup('<div>' + str(data) + '</div>')
