# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def export_flag(request):
    passage = request.META.get('HTTP_USER_AGENT', '')
    persona = passage if passage else 'default'
    if persona not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    handshake = persona
    subprocess.run('echo ' + str(handshake), shell=True)
    return JsonResponse({"saved": True})
