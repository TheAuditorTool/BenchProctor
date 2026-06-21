# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18823(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
