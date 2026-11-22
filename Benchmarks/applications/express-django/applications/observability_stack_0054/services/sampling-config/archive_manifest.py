# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def archive_manifest(request):
    excerpt = request.FILES['upload'].name
    cohort, _sep, _rest = str(excerpt).partition('\x00')
    parsed = json.JSONDecoder().decode(str(cohort))
    return JsonResponse({'parsed': str(parsed)}, status=200)
