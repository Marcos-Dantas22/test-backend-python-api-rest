# docs/marca_docs.py

create_marca_docs = {
    "summary": "Criar uma marca",
    "description": "Adiciona uma nova marca de veículos ao banco de dados.",
    "responses": {
        201: {"description": "Marca criada com sucesso"},
        400: {"description": "Erro de validação nos dados enviados ou marca já existe"},
    },
}

list_marcas_docs = {
    "summary": "Listar marcas",
    "description": "Retorna todas as marcas de veículos cadastradas no sistema.",
    "responses": {
        200: {"description": "Lista de marcas retornada com sucesso"},
    },
}

get_marca_docs = {
    "summary": "Obter marca por ID",
    "description": "Retorna os dados de uma marca específica pelo seu ID.",
    "responses": {
        200: {"description": "Marca encontrada"},
        404: {"description": "Marca não encontrada"},
    },
}

update_marca_docs = {
    "summary": "Atualizar marca",
    "description": "Atualiza os dados de uma marca existente.",
    "responses": {
        200: {"description": "Marca atualizada com sucesso"},
        400: {"description": "Erro de validação nos dados enviados ou marca já existe"},
        404: {"description": "Marca não encontrada"},
    },
}

delete_marca_docs = {
    "summary": "Deletar marca",
    "description": "Remove uma marca do banco de dados pelo seu ID.",
    "responses": {
        200: {"description": "Marca deletada com sucesso"},
        404: {"description": "Marca não encontrada"},
    },
}
