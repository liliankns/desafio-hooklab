filmes = [
    {"titulo": "O Senhor dos Anéis", "ano": 2001, "avaliacao": 8.8},
    {"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3},
    {"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6}
]

avaliacoes = [filme["avaliacao"] for filme in filmes]
media_avaliacoes = sum(avaliacoes) / len(avaliacoes)
print(f"A média das avaliações dos filmes é: {media_avaliacoes:.2f}")

filme_maior_avaliacao = max(filmes, key=lambda x: x["avaliacao"])
print(f"O título do filme com a maior avaliação é: {filme_maior_avaliacao['titulo']}")

filme_menor_avaliacao = min(filmes, key=lambda x: x["avaliacao"])
print(f"O ano de lançamento do filme com a menor avaliação é: {filme_menor_avaliacao['ano']}")