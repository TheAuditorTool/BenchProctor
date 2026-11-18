# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00353(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    reader = make_reader(config_value)
    data = reader()
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})
