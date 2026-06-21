# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01551(request):
    upload_name = request.FILES['upload'].name
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
