# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33326(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '{}'.format(auth_header)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
