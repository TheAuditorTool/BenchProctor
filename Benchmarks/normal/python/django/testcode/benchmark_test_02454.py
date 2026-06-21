# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02454(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
