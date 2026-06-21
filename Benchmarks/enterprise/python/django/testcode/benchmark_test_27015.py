# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27015(request):
    raw_body = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
