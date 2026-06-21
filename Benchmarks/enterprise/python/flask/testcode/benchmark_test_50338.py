# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest50338(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    return Markup('<div>' + str(data) + '</div>')
