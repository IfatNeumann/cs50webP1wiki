from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title.capitalize(),
        "content": util.get_entry(title)
    })

def search(request):
    query = request.GET.get('q').strip()
    content = util.get_entry(query)
    if content:
        return render(request, "encyclopedia/entry.html", {
            "title": query.capitalize(),
            "content": content
        })
    return render(request, "encyclopedia/search_results.html", {
        "entries": util.get_substring_results(query)
    })