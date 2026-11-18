# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def compact_revision(request):
    synopsis = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    byline = normalize(synopsis)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if byline not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    addendum = '/var/app/data/' + byline
    os.unlink(addendum)
    return JsonResponse({"saved": True})
