from django.shortcuts import render


def tasks(request):
    context = {}
    context['hello'] = ' You can choose between \'train\' and \'parallel train\'. ' \
                       'If you choose the \'parallel train\' you will need to fill the \'Device\' part. '
    return render(request, 'data_method.html', context)


def datasets(request):
    context = {}
    context['hello'] = 'Dataset name to run, can be a list of datasets with space like cora citeseer ppi. Supported datasets include \'cora\', \'citeseer\', \'pumbed\', \'PPI\', \'wikipedia\', \'blogcatalog\', \'flickr\'. '
    return render(request, 'data_method.html', context)