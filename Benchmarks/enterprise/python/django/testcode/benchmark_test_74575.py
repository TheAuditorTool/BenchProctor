# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74575(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
