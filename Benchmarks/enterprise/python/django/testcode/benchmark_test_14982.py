# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach
from urllib.parse import unquote


def BenchmarkTest14982(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
