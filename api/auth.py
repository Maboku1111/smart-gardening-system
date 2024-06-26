import jwt
from datetime import datetime, timedelta
from fastapi_users.authentication import BearerTransport
from .config import settings

class MongoDBRealmJWTAuthentication(BearerTransport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token_audience = settings.REALM_APP_ID
        self.secret = settings.JWT_SECRET_KEY
        self.lifetime_seconds = settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60
        self.cookie_name = "FARM_auth"
        self.cookie_secure = settings.SECURE_COOKIE

    async def _generate_token(self, user):
        payload = {
            "user_id": str(user.id),
            "sub": str(user.id),
            "aud": self.token_audience,
            "external_user_id": str(user.id),
            "exp": datetime.utcnow() + timedelta(seconds=self.lifetime_seconds)
        }
        token = jwt.encode(payload, self.secret, algorithm="HS256")
        return token

jwt_authentication = MongoDBRealmJWTAuthentication(tokenUrl="auth/jwt/login")






