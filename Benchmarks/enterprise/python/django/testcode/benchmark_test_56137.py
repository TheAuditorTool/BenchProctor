# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56137(request):
    raw_body = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    int(str(data))
    return JsonResponse({"saved": True})
