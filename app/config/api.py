from authlib.integrations.django_oauth2.resource_protector import return_error_response
from authlib.oauth2 import OAuth2Error
from ninja import NinjaAPI
from ninja.errors import AuthenticationError, _default_authentication_error
from auth0.views import router as auth0_router
from auth0.auth import resource_protector

api = NinjaAPI()

api.add_router("/", auth0_router)


@api.exception_handler(OAuth2Error)
def handle_oauth2_error(request, exc):
    return return_error_response(exc)


@api.exception_handler(AuthenticationError)
def handle_default_authentication_error(request, exc):
    """Ninja have some basic authentication checks before Authlib's checks
    which stopped Authlib from outputing a more detail exception message.
    This handler acts as a workaround to disable those checks.

    This assumes only AuthBearer is used in all endpoints.
    """
    try:
        # let Authlib figures out what the error type is
        resource_protector.acquire_token(request)
    except OAuth2Error as oauth2_exc:
        return return_error_response(oauth2_exc)
    # if no error in accuring token, return the default error
    return _default_authentication_error(request, exc, api)
