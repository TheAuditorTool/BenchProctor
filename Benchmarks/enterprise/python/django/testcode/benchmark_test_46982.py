# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest46982(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
