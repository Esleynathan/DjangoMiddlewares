
from django.http import HttpResponse

def middleware_forbiden(get_response):
    # Código de inicialização do Middleware
    def middleware(request):
        # Aqui vai o código a ser executado antes da view
        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

        #if request.META['REMOTE_ADDR'] == '127.0.0.1':
        #    return HttpResponse('Você está bloqueado.', status=403)

        response = get_response(request)

        if request.META['REMOTE_ADDR'] == '127.0.0.1':
            response.content = b'<h1>Acesso negado.</h1>'
            response.status_code = 403


        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Aqui vai o código a ser executado depois da view
        
        return response

    return middleware


#class MiddlewareForbiden:
#    def __init__(self, get_response):
#        self.get_response = get_response
        

#    def __call__(self, request):
   
#        response = self.get_response(request)

#        return response