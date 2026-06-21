# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def BenchmarkTest79099(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
