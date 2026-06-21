# SPDX-License-Identifier: Apache-2.0


def BenchmarkTest14245(path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
