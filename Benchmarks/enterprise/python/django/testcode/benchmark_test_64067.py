# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import tempfile


def BenchmarkTest64067(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
