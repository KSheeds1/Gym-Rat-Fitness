from django.shortcuts import render


def our_community(request):
    """ Renders the 'our community' page """

    return render(request, 'community/our_community.html')


def my_community(request):
    """ Render the 'my community' page """

    return render(request, 'community/my_community.html')
