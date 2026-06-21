# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12516(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
