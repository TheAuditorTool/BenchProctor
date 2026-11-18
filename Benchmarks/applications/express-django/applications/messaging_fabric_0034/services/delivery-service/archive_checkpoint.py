# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def archive_checkpoint(request):
    footnote = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(footnote)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if bulletin not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    heading = '/var/app/data/' + bulletin
    os.unlink(heading)
    return JsonResponse({"saved": True})
