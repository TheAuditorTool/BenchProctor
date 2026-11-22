# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def format_checkpoint(request):
    transcript = request.POST.get('field', '')
    addendum = (lambda v: v.strip())(transcript)
    if addendum not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    byline = addendum
    os.system('echo ' + str(byline))
    return JsonResponse({"saved": True})
