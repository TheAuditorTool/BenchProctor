# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73580(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
