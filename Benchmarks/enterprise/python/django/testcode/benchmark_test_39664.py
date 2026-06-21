# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39664(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % str(forwarded_ip)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
