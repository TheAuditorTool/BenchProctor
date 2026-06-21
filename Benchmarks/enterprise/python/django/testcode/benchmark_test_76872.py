# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76872(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '%s' % str(config_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
