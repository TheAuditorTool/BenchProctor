# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest04748(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
