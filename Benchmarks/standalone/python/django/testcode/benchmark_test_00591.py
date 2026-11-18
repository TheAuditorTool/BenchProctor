# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00591(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
