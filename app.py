import falcon
import links

api = application = falcon.API()

links = links.Links()

api.add_route('/links', links)
