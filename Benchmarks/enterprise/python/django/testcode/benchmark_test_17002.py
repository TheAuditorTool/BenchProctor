# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17002(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
