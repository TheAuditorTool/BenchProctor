# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path


def BenchmarkTest00048(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    Path('/var/app/data/' + str(data)).write_text('data')
    return JsonResponse({"saved": True})
