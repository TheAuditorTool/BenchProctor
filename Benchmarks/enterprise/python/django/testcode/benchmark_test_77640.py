# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77640(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
