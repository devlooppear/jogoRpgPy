import random

class Personagem:
    def __init__(self, nome, emoji, vida, ataque, defesa, habilidades):
        self.nome = nome
        self.emoji = emoji
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.habilidades = habilidades

    def mostrar_status(self):
        print(f"{self.emoji} {self.nome}: Vida {self.vida}, Ataque {self.ataque}, Defesa {self.defesa}")

    def usar_habilidade(self, habilidade, inimigo):
        if habilidade in self.habilidades:
            if habilidade == "Corte Poderoso":
                dano = max((self.ataque * 2) - inimigo['defesa'], 0)
                print(f"Você usou Corte Poderoso e causou {dano} de dano!")
                inimigo['vida'] -= dano
            elif habilidade == "Bloqueio":
                self.defesa += 1
                print("Sua defesa aumentou em 1 pontos!")
            elif habilidade == "Bola de Fogo":
                dano = 40
                print(f"Você usou Bola de Fogo e causou {dano} de dano!")
                inimigo['vida'] -= dano
            elif habilidade == "Escudo Mágico":
                self.defesa += 2
                print("Sua defesa aumentou em 2 pontos!")
            elif habilidade == "Tiro Preciso":
                dano = max(self.ataque - inimigo['defesa'], 0) + 10
                print(f"Você usou Tiro Preciso e causou {dano} de dano!")
                inimigo['vida'] -= dano
            elif habilidade == "Evasão":
                self.defesa += 2
                print("Sua defesa aumentou em 2 pontos!")

def evento_aleatorio(personagem):
    eventos = [
        {"descricao": "Achou uma poção. Beber?", "efeitos": [(10, "Vida aumentada."), (-10, "Vida diminuída.")]},
        {"descricao": "Achou uma espada. Pegar?", "efeitos": [(5, "Ataque aumentado."), (-5, "Ataque diminuído.")]}
    ]
    evento = random.choice(eventos)
    print(evento["descricao"])
    print("1: Sim")
    print("2: Não")
    escolha = input()

    if escolha == "1":
        efeito = random.choice(evento["efeitos"])
        if "poção" in evento["descricao"]:
            personagem.vida += efeito[0]
        else:
            personagem.ataque += efeito[0]
        print(efeito[1])

def desventura(personagem, fase):
    inimigos = [
        {'nome': "Dragão", 'emoji': "🐉", 'vida': 100, 'ataque': 40, 'defesa': 20},
        {'nome': "Lobo", 'emoji': "🐺", 'vida': 80, 'ataque': 35, 'defesa': 20},
        {'nome': "Bruxo", 'emoji': "🧙", 'vida': 95, 'ataque': 40, 'defesa': 30},
        {'nome': "Orc", 'emoji': "👹", 'vida': 80, 'ataque': 30, 'defesa': 10},
        {'nome': "Fantasma", 'emoji': "👻", 'vida': 85, 'ataque': 30, 'defesa': 10}
    ]
    inimigo = random.choice(inimigos)

    evento_aleatorio(personagem)

    print(f"\n🔵 Fase {fase} - Você encontrou um {inimigo['emoji']} {inimigo['nome']}!")
    personagem.mostrar_status()

    while personagem.vida > 0 and inimigo['vida'] > 0:
        print("\nO que você vai fazer?")
        print("1: Atacar")
        print("2: Fugir")
        for idx, habilidade in enumerate(personagem.habilidades):
            print(f"{idx + 3}: Usar {habilidade}")

        acao = input()
        if acao == "1":
            dano = max(personagem.ataque - inimigo['defesa'], 0)
            inimigo['vida'] -= dano
            print(f"Você atacou {inimigo['nome']} e causou {dano} de dano!")
        elif acao == "2":
            print("Você fugiu!")
            break
        elif int(acao) >= 3 and int(acao) <= 2 + len(personagem.habilidades):
            habilidade_idx = int(acao) - 3
            personagem.usar_habilidade(personagem.habilidades[habilidade_idx], inimigo)

        if inimigo['vida'] <= 0:
            print(f"Você derrotou o {inimigo['nome']}!")
            break

        dano_inimigo = max(inimigo['ataque'] - personagem.defesa, 0)
        personagem.vida -= dano_inimigo
        print(f"{inimigo['nome']} te atacou e você perdeu {dano_inimigo} pontos de vida!")

        if personagem.vida <= 0:
            print("Você morreu!")
            break

def main():
    while True:
        print("\n🎮 Bem-vindo ao Jogo de RPG! 🎮")
        print("\nEscolha seu personagem:")
        print("1: Guerreiro ⚔️")
        print("2: Mago 🔮")
        print("3: Arqueiro 🏹")
        escolha = input()

        if escolha == "1":
            personagem = Personagem("Guerreiro", "⚔️", 100, 25, 20, ["Corte Poderoso", "Bloqueio"])
        elif escolha == "2":
            personagem = Personagem("Mago", "🔮", 80, 30, 15, ["Bola de Fogo", "Escudo Mágico"])
        elif escolha == "3":
            personagem = Personagem("Arqueiro", "🏹", 90, 20, 18, ["Tiro Preciso", "Evasão"])
        else:
            print("Opção inválida!")
            continue

        fase = 1
        while personagem.vida > 0:
            desventura(personagem, fase)
            fase += 1

        print("\n😵 Você morreu! Quer tentar novamente?")
        print("1: Sim")
        print("2: Não")
        replay = input()
        if replay != "1":
            break

if __name__ == "__main__":
    main()