# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest65177():
    stdin_value = input('input: ')
    if stdin_value:
        data = stdin_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
