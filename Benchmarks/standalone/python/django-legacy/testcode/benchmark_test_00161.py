# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def BenchmarkTest00161(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
