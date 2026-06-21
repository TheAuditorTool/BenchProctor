# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76935(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
