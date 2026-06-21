# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import os
import time


def BenchmarkTest35074(request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    if time.time() > 1000000000:
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
