# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import os


def BenchmarkTest26540(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    return HttpResponse(Template(data).render(Context()))
