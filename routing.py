from channels.routing import ProtocolTypeRouter,URLRouter

from channels.auth import AuthMiddlewareStack

import chat.routing

application = ProtocolTypeRouter({
    #빈것은 http-> Django view로 가는 기본값
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
