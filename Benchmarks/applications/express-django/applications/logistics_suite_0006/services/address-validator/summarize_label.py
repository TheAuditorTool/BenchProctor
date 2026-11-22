# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def summarize_label(request, path_param):
    summary = request.path.split('/')[-1]
    if summary:
        consignment = summary
    else:
        consignment = ''
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(consignment)}))
    return HttpResponse(page)
