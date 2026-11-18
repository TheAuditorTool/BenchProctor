# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def verify_checkpoint(request):
    wording = request.META.get('HTTP_USER_AGENT', '')
    remark = wording if wording else 'default'
    if remark not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    phrase = remark
    subprocess.run('echo ' + str(phrase), shell=True)
    return JsonResponse({"saved": True})
