# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28957(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
