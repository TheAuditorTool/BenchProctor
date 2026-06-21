# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78329(request):
    upload_name = request.FILES['upload'].name
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
