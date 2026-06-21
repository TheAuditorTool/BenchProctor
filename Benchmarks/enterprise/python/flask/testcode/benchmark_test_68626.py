# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os


def BenchmarkTest68626():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    return Markup('<div>' + str(data) + '</div>')
