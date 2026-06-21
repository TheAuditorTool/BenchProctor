# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest03594(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
