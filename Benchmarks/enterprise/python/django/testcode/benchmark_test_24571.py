# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24571(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
