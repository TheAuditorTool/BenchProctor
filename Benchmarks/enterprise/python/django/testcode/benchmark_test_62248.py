# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62248(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
