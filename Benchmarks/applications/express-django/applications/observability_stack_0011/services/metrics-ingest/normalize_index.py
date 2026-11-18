# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def normalize_index(request):
    caption = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(caption)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if gauge not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    cohort = '/var/app/data/' + gauge
    os.unlink(cohort)
    return JsonResponse({"saved": True})
