# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def to_text(value):
    return str(value).strip()

def BenchmarkTest64106(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = to_text(forwarded_ip)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
