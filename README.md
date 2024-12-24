# Art, Video and GIF Pixelizer

Este é um projeto simples e divertido em Python que permite converter imagens, vídeos e GIFs em arte pixelada colorida diretamente no terminal.

Funcionalidades:
  - Imagens: Converte imagens estáticas em arte ASCII pixelada com cores baseadas na luminosidade.
  - GIFs: Renderiza GIFs animados quadro a quadro no terminal, com fluidez configurável.
  - Vídeos: Reproduz vídeos completos como arte ASCII no terminal, em tempo real.
  - Cores Dinâmicas: Utiliza diferentes cores para representar níveis de luminosidade, criando uma experiência mais rica e visual.
  - Configuração Personalizável:
    - Largura da arte (para ajustar o tamanho da saída no terminal).
    - Taxa de quadros por segundo (FPS) para vídeos e GIFs.
    - Lista de caracteres ajustável para definir o estilo da arte.

Bibliotecas:
  - Colorama: Para adicionar cores dinâmicas ao terminal.
  - MoviePy: Para manipular e processar vídeos e GIFs.
  - Pillow: Para trabalhar com imagens e redimensionamento.
  - OS: Para limpar o terminal entre os quadros da animação.
  - Time: Para controlar a reprodução dos quadros no terminal.
