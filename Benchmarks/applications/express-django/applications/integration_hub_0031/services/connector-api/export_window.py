# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def export_window(request):
    snippet = os.environ.get('INTEGRATIONS_INPUT_0031', '')
    handshake = snippet if snippet else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    paragraph = handshake
    subprocess.run('echo ' + str(paragraph), shell=True)
    return JsonResponse({"saved": True})
