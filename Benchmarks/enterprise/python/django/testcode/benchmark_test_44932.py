# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest44932(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
