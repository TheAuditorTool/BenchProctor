# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path
import json


def BenchmarkTest00240(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    Path(checked_path).write_text('data')
    return JsonResponse({"saved": True})
