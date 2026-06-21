# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest41507(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
