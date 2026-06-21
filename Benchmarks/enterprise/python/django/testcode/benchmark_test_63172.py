# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63172(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ' '.join(str(ua_value).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
