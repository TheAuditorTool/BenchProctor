# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def prune_release(request, path_param):
    summary = request.path.split('/')[-1]
    if summary:
        phrase = summary
    else:
        phrase = ''
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(phrase)}))
    return HttpResponse(page)
