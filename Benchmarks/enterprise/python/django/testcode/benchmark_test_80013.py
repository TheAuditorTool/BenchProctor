# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80013(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
