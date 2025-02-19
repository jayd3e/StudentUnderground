from pyramid_handlers import action
from studentunderground.forms.assignment.add import AddAssignmentSchema
from deform import Form
from deform.exception import ValidationFailure

class AssignmentHandler(object):

    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']

    @action(renderer='assignment/index.mako')
    def index(self):
        title = "S2S | Assignments"
        legend = "Assignments"
        return {'here':self.here,
                'title':title}
        
    @action(renderer='assignment/add.mako')
    def add(self):
        title = "S2S | Add Assignments"
        legend = "Add Assignment"
        
        schema = AddAssignmentSchema()
        form = Form(schema, buttons=('submit',))
    
        if 'submit' in self.request.POST:
            controls = self.request.POST.items()
            try:
                form.validate(controls)
            except ValidationFailure as e:
                return {'form':e.render(),
                        'here':self.here,
                        'title':title}
            return {'form':'OK'}

        return {'here':self.here,
                'title':title,
                'form':form.render()}