from fastapi_users.authentication import BearerTransport

bearer_transport = BearerTransport(
    # TODO: Update URL
    tokenUrl="auth/login",
)
