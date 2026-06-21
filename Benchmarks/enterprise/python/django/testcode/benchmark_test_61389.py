# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from urllib.parse import unquote


def BenchmarkTest61389(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
