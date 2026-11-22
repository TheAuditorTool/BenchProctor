# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00094(request):
    upload_name = request.FILES['upload'].name
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(upload_name).strip()
        case _:
            data = str(upload_name)
    parsed = json.loads(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
