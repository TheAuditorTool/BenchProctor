# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49421(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
