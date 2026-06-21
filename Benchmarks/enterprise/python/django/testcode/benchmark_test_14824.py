# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14824(request):
    upload_name = request.FILES['upload'].name
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
