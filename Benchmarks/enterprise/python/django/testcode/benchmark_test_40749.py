# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40749(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
