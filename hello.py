# -*- coding: utf-8 -*-
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    data = b"<br>Hello world\n</br><br>Pedic</br>"
    print(env)
    #a = [b'p'+x+'/p' for x in env["QUERY_STRING"].split('&')]
    #return [bytes(env["QUERY_STRING"],'utf-8')]
    #print([[bytes(x,'utf-8') for x in env["QUERY_STRING"].split('&')]])
    return [bytes(x+'</br>','utf-8') for x in env["QUERY_STRING"].split('&')]
    #return iter([a])
