# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02286(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
