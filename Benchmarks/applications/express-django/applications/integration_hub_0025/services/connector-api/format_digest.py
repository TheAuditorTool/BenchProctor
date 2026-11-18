# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def format_digest(request):
    footnote = request.META.get('HTTP_REFERER', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    subprocess.Popen('echo ' + str(handshake), shell=True).wait()
    return JsonResponse({"saved": True})
