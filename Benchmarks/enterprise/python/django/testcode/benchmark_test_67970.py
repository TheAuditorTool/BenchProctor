# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67970(request):
    xml_value = request.body.decode('utf-8')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
