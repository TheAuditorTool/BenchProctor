# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65857(request):
    upload_name = request.FILES['upload'].name
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
