from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.views.generic import TemplateView
from mptt.exceptions import InvalidMove
from mptt.forms import TreeNodeChoiceField
from mptt.forms import MoveNodeForm

from hierarchial_data.models import File

class HomePage(TemplateView):
    page = 'form.html'
    files = File.objects.all()[5]

    def get(self, request, *args, **kwargs):
        form = MoveNodeForm(self.files)
        # return render(request, self.page, {'nodes':File.objects.all()})
        return render(request, self.page, {'form': form, 'files': self.files, 'files_tree': File.objects.all()})
    
    def post(self, request, *args, **kwargs):
        form = MoveNodeForm(self.files, request.POST)
        if form.is_valid():
            try:
                print(form.data['target'])
                files = form.save()
                return HttpResponseRedirect('/')
            except InvalidMove:
                print('invalid')
                return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')
        