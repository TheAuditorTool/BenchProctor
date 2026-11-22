# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def merge_receipt(request):
    caption = request.GET.get('id', '')
    parts = []
    for token in str(caption).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    subprocess.run(['echo', handshake], shell=False)
    return JsonResponse({"saved": True})
