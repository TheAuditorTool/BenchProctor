# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00914(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
