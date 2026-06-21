# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def normalise_input(value):
    return value.strip()

def BenchmarkTest64320(request):
    upload_name = request.FILES['upload'].name
    data = normalise_input(upload_name)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
