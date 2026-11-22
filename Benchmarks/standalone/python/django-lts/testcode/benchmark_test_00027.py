# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00027(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = (lambda v: v.strip())(config_value)
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})
