from django.shortcuts import render
from markdown2 import markdown
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_entry(request, entry_name):
    entry_name = entry_name.lower()
    if util.get_entry(entry_name) is not None:
        return render(request, "encyclopedia/entry.html", {
            "entry_name": entry_name,
            "content": convert_markdown_to_html(util.get_entry(entry_name))
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "Sorry, no entry found for that specific term."
        })

