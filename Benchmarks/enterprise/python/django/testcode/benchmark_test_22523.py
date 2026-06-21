# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22523(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
