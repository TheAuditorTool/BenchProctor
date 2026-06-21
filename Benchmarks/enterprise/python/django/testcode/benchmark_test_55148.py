# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def to_text(value):
    return str(value).strip()

def BenchmarkTest55148(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = to_text(ua_value)
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return JsonResponse({"saved": True})
