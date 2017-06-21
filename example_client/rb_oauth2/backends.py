from urllib.parse import urljoin

from django.conf import settings

from social_core.backends.oauth import BaseOAuth2


class ReviewboardOAuth2Backend(BaseOAuth2):
    """An example OAuth2 backend for Review Board.

    You must define the ``SOCIAL_AUTH_REVIEWBOARD_URL`` in addition to
    ``SOCIAL_AUTH_REVIEWBOARD_CLIENT`` and ``SOCIAL_AUTH_REVIEWBOARD_SECRET``
    in your ``settings.py``.
    """

    name = 'reviewboard'

    REVIEWBOARD_URL = settings.SOCIAL_AUTH_REVIEWBOARD_URL
    AUTHORIZATION_URL = urljoin(REVIEWBOARD_URL, '/oauth2/authorize/')
    ACCESS_TOKEN_URL = urljoin(REVIEWBOARD_URL, '/oauth2/token/')
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_details(self, response):
        return {
            'email': response['email'],
            'fullname': response['fullname'],
            'first_name': response['first_name'],
            'last_name': response['last_name'],
            'username': response['username'],
        }

    def user_data(self, access_token, *args, **kwargs):
        session_rsp = self.get_json(
            urljoin(self.REVIEWBOARD_URL, '/api/session/'),
            headers={
                'Authorization': 'Bearer %s' % access_token,
            },
        )
        user_url = session_rsp['session']['links']['user']['href']
        user_rsp = self.get_json(
            user_url,
            headers={
                'Authorization': 'Bearer %s' % access_token,
            },
        )

        return user_rsp['user']

    def get_scope(self):
        """Return the required scopes.

        If more scopes are required, they can be defined in the
        ``SOCIAL_AUTH_REVIEWBOARD_SCOPE`` setting and they will be added to
        these.
        """
        return super().get_scope() + [
            'root:read',
            'user:read',
            'session:read',
        ]
