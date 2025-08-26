create_carro_docs = {
    "summary": "Criar um carro",
    "description": "Adiciona um novo carro ao banco de dados. Retorna erro 400 se já existir um carro com o mesmo nome.",
    "responses": {
        201: {"description": "Carro criado com sucesso"},
        400: {"description": "Erro de validação nos dados enviados"},
    },
}

list_carros_docs = {
    "summary": "Listar carros",
    "description": "Retorna todos os carros cadastrados no sistema.",
    "responses": {
        200: {"description": "Lista de carros retornada com sucesso"},
    },
}

get_carro_docs = {
    "summary": "Obter carro por ID",
    "description": "Retorna os dados de um carro específico pelo seu ID.",
    "responses": {
        200: {"description": "Carro encontrado"},
        404: {"description": "Carro não encontrado"},
    },
}

update_carro_docs = {
    "summary": "Atualizar carro",
    "description": "Atualiza os dados de um carro existente. Retorna erro 400 se o novo nome do carro já existir.",
    "responses": {
        200: {"description": "Carro atualizado com sucesso"},
        400: {"description": "Erro de validação"},
        404: {"description": "Carro não encontrado"},
    },
}

delete_carro_docs = {
    "summary": "Deletar carro",
    "description": "Remove um carro do banco de dados pelo seu ID.",
    "responses": {
        200: {"description": "Carro deletado com sucesso"},
        404: {"description": "Carro não encontrado"},
    },
}
