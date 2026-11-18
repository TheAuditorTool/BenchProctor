# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def resolve_batch(request):
    summary = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(summary)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if addendum not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    byline = '/var/app/data/' + addendum
    os.unlink(byline)
    return JsonResponse({"saved": True})
