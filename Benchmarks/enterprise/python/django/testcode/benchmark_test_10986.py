# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10986(request):
    upload_name = request.FILES['upload'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
