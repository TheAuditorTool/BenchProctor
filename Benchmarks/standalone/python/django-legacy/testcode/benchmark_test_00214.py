# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00214(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value!s}'
    parsed = json.JSONDecoder().decode(str(data))
    return JsonResponse({'parsed': str(parsed)}, status=200)
