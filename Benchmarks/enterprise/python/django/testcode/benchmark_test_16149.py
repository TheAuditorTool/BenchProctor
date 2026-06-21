# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16149(request):
    multipart_value = request.POST.get('multipart_field', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(multipart_value))
    return resp
