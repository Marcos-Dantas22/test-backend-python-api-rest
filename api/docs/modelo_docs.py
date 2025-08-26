create_modelo_docs = {
    "summary": "Criar um modelo",
    "description": "Adiciona um novo modelo de veículo ao banco de dados.",
    "responses": {
        201: {"description": "Modelo criado com sucesso"},
        400: {"description": "Erro de validação nos dados enviados ou modelo já existe"},
    },
}

list_modelos_docs = {
    "summary": "Listar modelos",
    "description": "Retorna todos os modelos de veículos cadastrados no sistema.",
    "responses": {
        200: {"description": "Lista de modelos retornada com sucesso"},
    },
}

get_modelo_docs = {
    "summary": "Obter modelo por ID",
    "description": "Retorna os dados de um modelo específico pelo seu ID.",
    "responses": {
        200: {"description": "Modelo encontrado"},
        404: {"description": "Modelo não encontrado"},
    },
}

update_modelo_docs = {
    "summary": "Atualizar modelo",
    "description": "Atualiza os dados de um modelo existente. Retorna erro 400 se o novo nome do modelo já existir.",
    "responses": {
        200: {"description": "Modelo atualizado com sucesso"},
        400: {"description": "Erro de validação nos dados enviados ou modelo já existe"},
        404: {"description": "Modelo não encontrado"},
    },
}

delete_modelo_docs = {
    "summary": "Deletar modelo",
    "description": "Remove um modelo do banco de dados pelo seu ID.",
    "responses": {
        200: {"description": "Modelo deletado com sucesso"},
        404: {"description": "Modelo não encontrado"},
    },
}
