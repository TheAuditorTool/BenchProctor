# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31945(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
