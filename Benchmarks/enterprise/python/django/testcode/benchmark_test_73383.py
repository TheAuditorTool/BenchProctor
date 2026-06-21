# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73383(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
