# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00187(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
