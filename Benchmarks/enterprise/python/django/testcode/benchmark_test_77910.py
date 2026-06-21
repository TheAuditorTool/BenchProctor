# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77910(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
