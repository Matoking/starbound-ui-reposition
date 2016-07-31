from django.shortcuts import render, redirect
from django.http import HttpResponse

from forms import DownloadModForm

from starbound_ui_reposition.patch import create_mod


SCREEN_PRESETS = [
    {
        "name": "Three 1080p monitors",
        "values": (0, 1920, 0, 1920)
    },
    {
        "name": "Three 1440p monitors",
        "values": (0, 2560, 0, 2560)
    },
    {
        "name": "Three 4K monitors (damn)",
        "values": (0, 3840, 0, 3840)
    },
]


def index(request):
    form = DownloadModForm(request.POST or None)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        zip_data = create_mod({
            "top": cleaned_data["top"],
            "right": cleaned_data["right"],
            "bottom": cleaned_data["bottom"],
            "left": cleaned_data["left"]
        })

        response = HttpResponse(zip_data, content_type="application/zip")
        response["Content-Disposition"] = "attachment; filename=ui_reposition.zip"
        response["Content-Length"] = len(zip_data)
        return response

    return render(request, "index.html", {
        "presets": SCREEN_PRESETS
    })
