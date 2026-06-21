# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32335(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
