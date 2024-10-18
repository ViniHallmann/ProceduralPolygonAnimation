# **Procedural Polygon Animation**

Esses ultimos dias eu estava procurando por inspirações de perfis no github pra mudar um pouco meu perfil. Achei vários designs legais mas um em especifico me agradou. Na real não é o perfil em si, mas sim a introdução logo de inicio.

Esse aqui é o GIF que aparece logo no inicio do perfil do usuário:

![referência](https://github.com/adamalston/adamalston/raw/master/profile.gif)

Olhando isso pensei que seria legal fazer algo semelhante em Python. Usando PyGame consegui gerar uma animação procedural bem parecida com a referência. A animação é criada a partir de pontos que se movem aleatoriamente, e as conexões entre esses pontos são desenhadas quando eles estão próximos o suficiente. Isso resulta em uma visualização interessante e dinâmica.

![Resultado](assets/result4.gif)

### **Como funciona o código**:
- Um número fixo de pontos é gerado aleatoriamente na tela.
- Esses pontos se movem com velocidades também aleatórias.
- Linhas são desenhadas entre pontos que estão a uma distância menor que um valor predefinido.
- A animação é atualizada constantemente, criando um efeito dinâmico e procedural.

Sinta-se à vontade para explorar e modificar o código para personalizar o efeito visual!

### **Personalização:**
- Para alterar as informações de exibição, como nome e título, basta modificar as variáveis **`NAME_TEXT`** e **`TITLE_TEXT`**. Tenha cuidado ao usar textos longos, pois o código não trata o layout para grandes tamanhos de texto, o que pode desformatar a centralização.
- Você também pode ajustar:
  - O raio dos pontos
  - A velocidade
  - A quantidade de pontos
  - A distância mínima para a conexão entre dois pontos.

 ### **Falta fazer:**

 - ~~Suaviação do desenho da linha conforme a distancia entre dois pontos aumenta~~
 - Refatoração num geral
 - Responsividade no layout para diferentes textos
 - Melhoria na performance caso o programa esteja calculando para mais de 125 pontos
