# Servidor HTTP del TP Final: formulario de LOGIN con GET y POST
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

USUARIOS = {"admin": "1234"}

FORM = """<html><head><meta charset="utf-8"><title>Login - petas.izo</title></head><body>
<h2>Login - petas.izo</h2>
<h3>Envio por POST (los datos van en el cuerpo)</h3>
<form method="POST" action="/login">
  Usuario: <input name="user"><br>
  Clave: <input name="pass" type="password"><br>
  <input type="submit" value="Entrar (POST)">
</form>
<h3>Envio por GET (los datos van en la URL)</h3>
<form method="GET" action="/login">
  Usuario: <input name="user"><br>
  Clave: <input name="pass" type="password"><br>
  <input type="submit" value="Entrar (GET)">
</form>
</body></html>"""

class Handler(BaseHTTPRequestHandler):
    def responder(self, codigo, cuerpo):
        datos = cuerpo.encode()
        self.send_response(codigo)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(datos)))
        self.end_headers()
        self.wfile.write(datos)

    def validar(self, params, metodo):
        user = params.get("user", [""])[0]
        clave = params.get("pass", [""])[0]
        if user and USUARIOS.get(user) == clave:
            return 200, f"<h2>Login correcto</h2><p>Bienvenido {user} (metodo {metodo})</p>"
        return 401, f"<h2>Login incorrecto</h2><p>Usuario o clave invalidos (metodo {metodo})</p>"

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/":
            self.responder(200, FORM)
        elif url.path == "/login":
            self.responder(*self.validar(parse_qs(url.query), "GET"))
        else:
            self.responder(404, "<h2>No encontrado</h2>")

    def do_POST(self):
        if self.path != "/login":
            return self.responder(404, "<h2>No encontrado</h2>")
        largo = int(self.headers.get("Content-Length", 0))
        cuerpo = self.rfile.read(largo).decode()
        self.responder(*self.validar(parse_qs(cuerpo), "POST"))

HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
