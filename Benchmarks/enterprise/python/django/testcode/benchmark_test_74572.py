# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74572(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    eval(str(data))
    return JsonResponse({"saved": True})
