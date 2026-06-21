# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
import os


def BenchmarkTest20880(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
