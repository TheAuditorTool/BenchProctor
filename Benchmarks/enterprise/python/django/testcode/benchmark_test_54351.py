# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import os


def BenchmarkTest54351(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    return HttpResponse(Template(data).render(Context()))
