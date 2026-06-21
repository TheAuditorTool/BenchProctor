# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02515(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
