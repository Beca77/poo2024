class Usuario:
    def __init__(self, nome, username, email, fone, playlist = 0):
        self.nome = nome
        self.username = username
        self.email = email
        self.fone = fone
        self.playlist = playlist


#aqui o usuario criará sua conta, adicionando os criterios pedidos

class Musica:
    def __init__(self, titulo, genero, duracao, categoria):
        self.titulo = titulo
        self.genero = genero
        self.duracao_msc = duracao
        self.categoria = categoria


class Playlist:
    def __init__(self,titulo):
        self.titulo = titulo
        self.duracao = 0
        self.mscs = []

    def add_msc(self, msc):
        self.mscs.append(msc)
        self.duracao += msc.duracao_msc

    def remove_song(self, msc):
        if msc in self.mscs:
            self.mscs.remove(msc)
            self.duracao -= msc.duracao_msc
        else:
            print("A música não está na playlist.")


musica = Musica("Broken Heart ", "Phonky ", 240, "Phonky" )

pl01 = Playlist("Phonky")

print("Duração:", pl01.duracao)

pl01.add_msc(musica)

print("Duração:", pl01.duracao)

pl01.add_msc(musica)

print("Duração:", pl01.duracao)

musica1 = Musica("Broken dreans", "Lofi", 120, "Lofi")

print("Duração:", pl01.duracao)

pl01.add_msc(musica)

print("Duração:", pl01.duracao)

musica2 = Musica("Fearl ees", "Pop", 180, "Pop")

print("Duração:", pl01.duracao)

pl01.add_msc(musica)

print("Duração:", pl01.duracao)

