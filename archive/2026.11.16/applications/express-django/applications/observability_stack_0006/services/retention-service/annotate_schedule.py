# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def annotate_schedule(request):
    preface = request.GET.get('id', '')
    cohort, _sep, _rest = str(preface).partition('\x00')
    parsed = yaml.safe_load(cohort)
    return JsonResponse({'parsed': str(parsed)}, status=200)
