# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32820(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
