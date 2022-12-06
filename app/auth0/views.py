from ninja import Router

from auth0.auth import AuthBearer


router = Router()


@router.get('/public')
def public(request):
    """No access token required to access this route"""
    response = "Hello from a public endpoint! You don't need to be authenticated to see this."
    return dict(message=response)


@router.get('/private', auth=AuthBearer())
def private(request):
    """A valid access token is required to access this route"""

    response = "Hello from a private endpoint! You need to be authenticated to see this."
    return dict(
        user=str(request.user.id),
        oauth_token=request.oauth_token,
        message=response,
    )


@router.get('/private-scoped', auth=AuthBearer('read:messages'))
def private_scoped(request):
    """A valid access token and an appropriate scope are required to access this route"""
    response = "Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this."
    return dict(
        user=str(request.user.id),
        oauth_token=request.oauth_token,
        message=response,
    )
