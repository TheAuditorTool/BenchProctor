# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def BenchmarkTest15459(request):
    upload_name = request.FILES['upload'].name
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(upload_name))
    return JsonResponse({"saved": True})
