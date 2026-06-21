# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path
import ast


def BenchmarkTest07718(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
