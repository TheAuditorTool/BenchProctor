# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def prune_syndication(request):
    transcript = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(transcript)
    if addendum not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    byline = addendum
    os.system('echo ' + str(byline))
    return JsonResponse({"saved": True})
