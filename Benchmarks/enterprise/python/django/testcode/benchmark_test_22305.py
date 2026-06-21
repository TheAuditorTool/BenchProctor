# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22305(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
