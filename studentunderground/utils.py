from mako.template import Template

def mako_renderer(template_name, **kw):
    template = Template(filename='studentunderground/templates/forms/%s.mako' % template_name)
    return template.render(**kw)