from django.shortcuts import render


# Create your views here.
def about(request):
    """Страница, отображающая информацию о проекте."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Страница, отображающая информацию о наших правилах."""
    template = 'pages/rules.html'
    return render(request, template)
