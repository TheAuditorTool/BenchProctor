# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest80192(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '%s' % (json_value,)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
