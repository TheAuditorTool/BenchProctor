# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11520(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    prefix = ''
    data = prefix + str(auth_header)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
