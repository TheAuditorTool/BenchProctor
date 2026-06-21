# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21207(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip}'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
