# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def summarize_profile(request):
    caption = request.POST.get('field', '')
    remittance = (lambda v: v.strip())(caption)
    if remittance not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    dunning = remittance
    os.system('echo ' + str(dunning))
    return JsonResponse({"saved": True})
