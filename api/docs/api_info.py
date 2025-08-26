api_title = "API de Carros"
api_description = """
API para gerenciamento de marcas, modelos e carros.

Inclui criação, listagem, atualização e exclusão de registros.
Todas as validações de unicidade e integridade referencial são tratadas no backend.
"""
api_version = "1.0.0"

api_contact = {
    "name": "Marcos Vinícius",
    "url": "https://github.com/Marcos-Dantas22",  # seu link ou site
    "email": "marcosdantaslkdin@gmail.com"
}

api_servers = [
    {"url": "http://localhost:8000", "description": "Servidor local"},
    {"url": "https://api.seusite.com", "description": "Servidor de produção"}
]
