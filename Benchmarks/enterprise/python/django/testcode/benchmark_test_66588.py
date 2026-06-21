# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66588(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
