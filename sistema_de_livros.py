import matplotlib.pyplot as plt

# Classe que representa um livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

# Lista para armazenar os livros cadastrados
biblioteca = []

# Função para cadastrar livro
def cadastrar_livro(titulo, autor, genero, quantidade):
    livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")

# Função para listar todos os livros
def listar_livros():
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    else:
        print("\n--- Lista de livros ---")
        for livro in biblioteca:
            print(f"Título: {livro.titulo} | Autor: {livro.autor} | "
                  f"Gênero: {livro.genero} | Quantidade: {livro.quantidade}")

# Função para buscar livro pelo título
def buscar_livro(titulo):
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            return f"Livro encontrado: {livro.titulo} - {livro.autor}"
    return "Livro não encontrado."

# Função para gerar gráfico
def gerar_grafico():
    if not biblioteca:
        print("Nenhum livro cadastrado para gerar gráfico.")
        return
    
    generos = {}
    for livro in biblioteca:
        generos[livro.genero] = generos.get(livro.genero, 0) + livro.quantidade
    
    plt.bar(generos.keys(), generos.values(), color='skyblue')
    plt.xlabel("Gêneros")
    plt.ylabel("Quantidade de livros")
    plt.title("Quantidade de Livros por Gênero")
    plt.show()

# Testando o sistema
cadastrar_livro("Dom Casmurro", "Machado de Assis", "Romance", 3)
cadastrar_livro("O Alienista", "Machado de Assis", "Ficção", 2)
cadastrar_livro("Python para Iniciantes", "Fulano de Tal", "Tecnologia", 5)

listar_livros()
print(buscar_livro("Dom Casmurro"))
print(buscar_livro("Livro Inexistente"))
gerar_grafico()