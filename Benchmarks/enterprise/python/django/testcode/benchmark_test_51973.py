# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51973(request):
    xml_value = request.body.decode('utf-8')
    return JsonResponse({'error': str(xml_value), 'stack': repr(locals())}, status=500)
