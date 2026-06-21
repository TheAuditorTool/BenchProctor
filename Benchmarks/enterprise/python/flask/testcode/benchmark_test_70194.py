# SPDX-License-Identifier: Apache-2.0


request_state: dict[str, str] = {}

def BenchmarkTest70194(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
