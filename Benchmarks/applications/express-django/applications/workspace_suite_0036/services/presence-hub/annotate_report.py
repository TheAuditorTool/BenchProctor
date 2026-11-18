# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def annotate_report(request):
    remark = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    synopsis = normalize(remark)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if synopsis not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    quotation = '/var/app/data/' + synopsis
    os.unlink(quotation)
    return JsonResponse({"saved": True})
