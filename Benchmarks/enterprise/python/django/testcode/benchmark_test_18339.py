# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18339(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value}'
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
