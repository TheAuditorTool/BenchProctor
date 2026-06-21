# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06627(request):
    raw_body = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
