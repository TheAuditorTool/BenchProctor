# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72651(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
