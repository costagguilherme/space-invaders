
# Space Invaders
#### Game inspirado no clássico "Space Invaders". Basicamente, o objetivo é destruir os inimigos e impedir a invasão do espaço.

### Orientações
* É necessário instalar 3 bibliotecas: Tupy, Mypy e Pygame.
* Rodar o jogo com "python main.py".
* As setas movimentam a nave e a tecla espaço atira.

### Equipe
Todos os integrantes participaram de todo processo de criação do jogo (Estrutura das classes, código, imagens).

* Guilherme Costa Lopes (Contribuição 5)
* Letícia Santos Teixeira (Contribuição 5)
* Lucas Perrone (Contribuição 5)
* Matheus Nascimento (Contribuição 5)
* Vitor Hugo (Contribuição 5)

## Classes

#### Classe Enemie
- Representa o inimigo

#### Classe SpaceShip
- Representa a nave
- **Update**:  Faz a movimentação da nave

#### Classe Shot
- Representa o tiro
- **Update**:  Verifica a coalisão do tiro da nave com o inimigo

#### Classe EnemieShot
- Representa o tiro do inimigo
- **Update**:  Verifica a coalisão do tiro inimigo com a nave

#### Classe Wall
- Representa o obstáculo
- **Update**:  Faz a movimentação do obstáculo

#### Classe Life
- Representa a vida da nave
- **Update**:  Alterna as imagens da vida

#### Classe Battlefield
- Representa o campo de batalha
- Orquestra todas as outras classes
- **Update**: Gera os tiros da nave, verifica a coalisão dos tiros da nave com o tiro inimigo e faz o update de outras 3 classes (Shot, EnemieShot e Wall)

#### Outras classes
* Além disso temos outras classes acessórias
* Audio: Responsável pelo aúdio do jogo
* Timer: Representa um relógio
