# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34142(request):
    upload_name = request.FILES['upload'].name
    ciphertext = bytes(b ^ 0x42 for b in str(upload_name).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
