# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00200(request):
    field_value = request.POST.get('field', '')
    data = '%s' % str(field_value)
    parsed = json.loads(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
