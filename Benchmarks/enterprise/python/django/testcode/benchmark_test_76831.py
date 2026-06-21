# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76831(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
