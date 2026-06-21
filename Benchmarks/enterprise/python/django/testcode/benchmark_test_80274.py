# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80274(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
