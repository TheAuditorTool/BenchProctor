# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest20378(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
