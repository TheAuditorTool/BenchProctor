# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00164(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
