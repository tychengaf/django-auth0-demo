from authlib.integrations.django_oauth2 import ResourceProtector
from authlib.oauth2.rfc6749 import MissingAuthorizationError
from django.conf import settings
from ninja.security import HttpBearer

from auth0.models import Auth0User as User
from auth0.validators import Auth0JWTBearerTokenValidator


resource_protector = ResourceProtector()

validator = Auth0JWTBearerTokenValidator(
    settings.AUTH0_DOMAIN,
    settings.AUTH0_AUDIENCE,
)

resource_protector.register_token_validator(validator)


class AuthBearer(HttpBearer):
    def __init__(
        self,
        scopes: str | list[str] | None = None,
        optional: bool = False,
    ):
        super().__init__()
        self.scopes = scopes
        self.optional = optional

    def ___call__(self, request):
        return self.authenticate(request, None)

    def authenticate(self, request, token):
        try:
            token = resource_protector.acquire_token(request, self.scopes)
        except MissingAuthorizationError:
            if self.optional:
                request.oauth_token = None
            raise
        user, _ = User.objects.get_or_create(sub=token['sub'])
        request.oauth_token = token
        request.user = user
        return token
