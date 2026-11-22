# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def annotate_snapshot(request):
    paragraph = request.POST.get('field', '')
    wording = (lambda v: v.strip())(paragraph)
    if wording not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    transcript = wording
    os.system('echo ' + str(transcript))
    return JsonResponse({"saved": True})
