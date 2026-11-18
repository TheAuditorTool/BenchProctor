# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00602(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    if config_value:
        data = config_value
    else:
        data = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return JsonResponse({"saved": True})
