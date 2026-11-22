# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from pathlib import Path


def BenchmarkTest00084(request, path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(path_value).strip()
        case _:
            data = str(path_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    Path('/var/app/data/' + str(processed)).write_text('data')
    return JsonResponse({"saved": True})
