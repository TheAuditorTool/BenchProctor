# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def verify_manifest(request):
    citation = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(citation)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if parcel not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    consignment = '/var/app/data/' + parcel
    os.unlink(consignment)
    return JsonResponse({"saved": True})
