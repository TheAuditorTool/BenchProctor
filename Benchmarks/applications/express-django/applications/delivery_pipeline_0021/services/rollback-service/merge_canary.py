# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def merge_canary(request):
    summary = request.POST.get('field', '')
    phrase = (lambda v: v.strip())(summary)
    if phrase not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    subtitle = phrase
    os.system('echo ' + str(subtitle))
    return JsonResponse({"saved": True})
