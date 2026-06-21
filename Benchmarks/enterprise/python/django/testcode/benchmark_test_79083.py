# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79083(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = str(forwarded_ip).replace('\x00', '')
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
