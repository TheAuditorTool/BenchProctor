# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest12860(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    return HttpResponse(Template(data).render(Context()))
