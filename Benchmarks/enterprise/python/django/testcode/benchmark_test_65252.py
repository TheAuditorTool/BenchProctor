# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65252(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = config_value if config_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
