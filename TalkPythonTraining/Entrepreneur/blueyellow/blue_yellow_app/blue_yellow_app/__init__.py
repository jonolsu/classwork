from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=60*60*24*365)
    config.add_route('home', '/')
    config.add_route('albums', '/')
    config.add_route('album', '/albums/{name_fragment}')
    config.add_route('store', '/buy/{name_fragment}')
    config.scan()
    return config.make_wsgi_app()

#@view_config(route_name='home',
#             renderer='templates/albums.pt')

def index(request):
    albums = [
        {'has preview': True, 'title': 'Digital ...', 'url': '/album/123'},
        {'has preview': True, 'title': 'Freedom songs', 'url': '/album/993'},
        {'has preview': False, 'title': 'Makin money', 'url': '/album/722'}
    ]
    return {'albums':albums}
