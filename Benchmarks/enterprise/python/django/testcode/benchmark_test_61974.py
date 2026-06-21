# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61974(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(config_value)
    data = collected
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
