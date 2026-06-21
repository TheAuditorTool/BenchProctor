# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def BenchmarkTest39250(request):
    upload_name = request.FILES['upload'].name
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return JsonResponse({"saved": True})
