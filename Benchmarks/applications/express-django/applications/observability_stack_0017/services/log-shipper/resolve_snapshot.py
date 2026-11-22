# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def resolve_snapshot(request):
    note = request.FILES['upload'].name
    cohort, _sep, _rest = str(note).partition('\x00')
    parsed = json.JSONDecoder().decode(str(cohort))
    return JsonResponse({'parsed': str(parsed)}, status=200)
