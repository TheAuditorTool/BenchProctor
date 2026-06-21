# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest55984(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
