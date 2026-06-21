# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os


def BenchmarkTest09739():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    return Markup('<div>' + str(data) + '</div>')
