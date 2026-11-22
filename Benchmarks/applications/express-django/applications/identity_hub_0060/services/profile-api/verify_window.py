# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def verify_window(request):
    paragraph = request.GET.get('id', '')
    parts = []
    for token in str(paragraph).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    subprocess.run(['echo', persona], shell=False)
    return JsonResponse({"saved": True})
