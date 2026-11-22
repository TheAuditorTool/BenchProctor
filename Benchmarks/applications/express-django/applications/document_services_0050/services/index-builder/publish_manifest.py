# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def publish_manifest(request):
    citation = request.FILES['upload'].name
    dossier, _sep, _rest = str(citation).partition('\x00')
    parsed = json.JSONDecoder().decode(str(dossier))
    return JsonResponse({'parsed': str(parsed)}, status=200)
