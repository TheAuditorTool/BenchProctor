# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01352(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
