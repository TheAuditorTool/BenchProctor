# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21727(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
