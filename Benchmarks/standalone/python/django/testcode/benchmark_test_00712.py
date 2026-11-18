# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00712(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '%s' % (config_value,)
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return JsonResponse({"saved": True})
