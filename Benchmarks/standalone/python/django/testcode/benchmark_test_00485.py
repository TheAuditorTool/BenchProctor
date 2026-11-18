# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00485(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(file_value)
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})
