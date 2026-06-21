# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01467(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
