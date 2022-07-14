# Redes
Analise de vídeos em redes Wi-Fi

Este repositório contêm documentos com o resultado de testes de vídeos em Redes Wi-Fi. 

A analise foi feita emulando os seguintes cenários:
  Vídeos em momento de estabilidade da Rede
  Livestream em momentos de estabilidade da Rede
  Vídeos em momento de congestionamento da Rede
  
Ferramentas Utilizadas:
  Ferramenta nativa do Youtube de Analise de vídeos
  Wiresahrk
  Python
  
Com esses testes se obteve o comportamento da rede em tais cenários utilizando a ferramenta nativa de estatistica de vídeos do Youtube, testes capturados no Wireshark e testes realizados em um código Python de autoria própria. Em paralelo, conseguimos também observar como os principais protocolos da camada de transporte funcionam(TCP, UDP e, no caso do youtube, QUIC).

Principalmente no protocolo TCP onde se observou como a velocidade de banda permite que se utilize esse protocolo apesar de todos seus "problemas" para aplicações em tempo real(Slow-Start, 3-way Handshake, etc...). Adicionalmente, observamos também como o avanço da velocidade de banca culminou no protocolo QUIC, que busca utilizar o melhor do TCP e UDP em um mesmo protocolo.

Foi observado também como esses protocolos mitigam problemas de banda nos seus respectivos cenários através de uma analise do Buffer.

Autoria:
  Mathews Vaz Reis
  Palloma da Silva Machado Nunes
  Thais Moylany da Silva Rocha
  



