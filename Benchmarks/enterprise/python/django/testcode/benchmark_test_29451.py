# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29451(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
