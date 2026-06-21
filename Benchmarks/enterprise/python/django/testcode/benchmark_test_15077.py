# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15077(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
