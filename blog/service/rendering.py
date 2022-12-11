

def render_response(renderOBJ):
    renderOBJ['Cache-Control'] = "no-cache, no-store, must-revalidate"
    renderOBJ['Pragma'] = 'no-cache'
    return renderOBJ