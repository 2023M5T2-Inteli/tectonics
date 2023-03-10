<table>
<tr>
<td>
<a href= "https://www.ipt.br/"><img src="https://www.ipt.br/imagens/logo_ipt.gif" alt="IPT" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12"><center>
Magnetum | Concepção de sistema de automação industrial para separação magnética (IPT)
</center></font>

**Conteúdo**

- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
  - [Empresa](#empresa)
  - [O Problema](#o-problema)
  - [Objetivos](#objetivos)
    - [Objetivos gerais](#objetivos-gerais)
    - [Objetivos específicos](#objetivos-específicos)
  - [Partes interessadas](#partes-interessadas)
- [Análise do Problema](#análise-do-problema)
  - [Matriz de Risco](#matriz-de-risco)
  - [Oceano Azul](#oceano-azul)
  - [Análise financeira](#análise-financeira)
  - [Proposta de Valor: Value Proposition Canvas](#proposta-de-valor-value-proposition-canvas)
  - [Personas](#personas)
  - [Histórias dos usuários (user stories)](#histórias-dos-usuários-user-stories)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Diagrama geral](#diagrama-geral)
  - [Projeto mecânico](#projeto-mecânico)
  - [Projeto eletrônico](#projeto-eletrônico)
    - [Esquemático do circuito](#esquemático-do-circuito)
    - [Implementação do circuito](#implementação-do-circuito)
      - [Componentes utilizados](#componentes-utilizados)
      - [Validação dos dispositivos eletrônicos](#validação-dos-dispositivos-eletrônicos)
  - [Módulos do Sistema e Visão Geral (Big Picture)](#módulos-do-sistema-e-visão-geral-big-picture)
  - [Descrição dos Subsistemas](#descrição-dos-subsistemas)
    - [Descrição dos componentes](#descrição-dos-componentes)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
    - [Testes de componentes](#testes-de-componentes)
      - [Movimentação do robô](#movimentação-do-robô)
      - [Eletroímã na ponte H](#eletroímã-na-ponte-h)
      - [Bomba d'água na ponte H](#bomba-dágua-na-ponte-h)
      - [Sensor de campo eletromagnético](#sensor-de-campo-eletromagnético)
      - [Célula de carga e amplificador HX711](#célula-de-carga-e-amplificador-hx711)
    - [Relatório de entradas e saídas dos testes](#relatório-de-entradas-e-saídas-dos-testes)
- [UX e UI Design](#ux-e-ui-design)
- [Projeto de Banco de Dados](#projeto-de-banco-de-dados)
  - [Modelo Conceitual](#modelo-conceitual)
  - [Modelo Lógico](#modelo-lógico)
- [Teste de Software](#teste-de-software)
  - [Testes Unitários](#testes-unitários)
  - [Teste de Usabilidade](#teste-de-usabilidade)
- [Análise de Dados](#análise-de-dados)
- [Manuais](#manuais)
  - [Manual de Implantação](#manual-de-implantação)
  - [Manual do Usuário](#manual-do-usuário)
  - [Manual do Administrador](#manual-do-administrador)
- [Referências](#referências)


# Autores

* Antônio Ribeiro Cavalcante
* Elisa de Oliveira Flemer
* Emanuele Lacerda Morais Martins
* Felipe Campos
* Henrique Agostinho Schilder Lima
* João Vitor Oliveira Rodrigues
* Luca Sarhan Giberti


# Visão Geral do Projeto

## Empresa

O Instituto de Pesquisas Tecnológicas (IPT) é uma instituição de pesquisa brasileira que tem como objetivo contribuir para o desenvolvimento científico, tecnológico e insdustrial do país. Fundado em 1899, é um dos mais antigos centros de pesquisa tecnológica do país e tem uma ampla variedade de áreas de atuação. O instituto possui uma ampla infraestrutura de laboratórios e centros de pesquisa, com equipamentos de última geração e uma equipe multidisciplinar de pesquisadores, engenheiros, técnicos e especialistas. Além disso, realiza parcerias com empresas e instituições de pesquisa nacionais e internacionais, visando a transferência de tecnologia e a cooperação científica.

## O Problema

O IPT possui uma área de atuação em materiais avançados e a separação magnética é uma técnica comumente utilizada para avaliar a liberação de minerais e materiais com propriedades magnéticas. Entretanto, devido ao processo de separação magnética ser manual, a medição da distância não é precisa, o que afeta diretamente a precisão do campo eletromagnético aplicado às partículas. Como o campo eletromagnético é inversamente proporcional à distância, a determinação do campo correto para separar os minerais se torna complicada. Além disso, para experimentar diferentes campos, é preciso alternar os ímãs utilizados, requerendo uma variedade de ímãs disponíveis.

## Objetivos

### Objetivos gerais

É necessário desenvolver um equipamento automatizado capaz de aplicar um campo magnético constante, com intensidade e distância ajustáveis, sobre toda a amostra. Isso permitirá separar os minerais magnéticos, que serão depositados em um recipiente diferente dos minerais não magnéticos, que permanecerão na bandeja original.

### Objetivos específicos

O projeto objetiva a automatização dos ensaios de separação magnética de amostras de minerais, por meio de um braço mecânico capaz de coletar, limpar e despejar o material captado. Esse processo visa aumentar a produtividade, repetibilidade, eficiência e precisão dos ensaios. Para isso, foi utilizado um  braço mecânico (Dobot Magician Lite),um eletroímã com intensidade ajustável para diferentes tipos de minerais e sensores capazes de detectar o peso do material extraído e medir o fluxo magnético produzido pelo eletroímã.

## Partes interessadas

* Laboratório de processo metalúrgicos;
* Inteli

# Análise do Problema

Para melhor entender o contexto do projeto, realizamos uma análise de Oceano Azul para identificar nosso posicionamento em relação ao método tradicional de separação magnético. Buscamos também concorrentes, como o HGMS da empresa Metso, mas concluímos que sua aplicação não servia ao mesmo nicho que nosso projeto.

Ademais, criamos uma matriz de risco sobre o desenvolvimento do projeto, com base em nossas experiências conjuntas de riscos e oportunidades de módulos passados aplicados às possibilidades do bimestre vigente. 

Por fim, a partir da análise das informações citadas acima e dados obtidos do entendimento do design, sintetizamos o canvas de proposta de valor da solução

## Matriz de Risco

![image](https://user-images.githubusercontent.com/99221221/221010837-95321191-ad6f-4ac9-a3ca-75cc505b2966.png)

Riscos análisados:
* 1 - Danificar o Magician Lite
* 2 - Demora do parceiro fornecer materiais necessários
* 3 - Incapacidade de realizar testes fidedignos à demanda do projeto
* 4 - Queima de componentes eletrônicos
* 5 - Conflito de merge no GIT
* 6 - Ausência de membros
* 7 - Falta de comunicação
* 8 - Incerteza com a expectativa dos entregáveis
* 9 - Viés na análise das amostras
* 10 - O MVP ser adotado pelo parceiro
* 11 - Aumento significativo da velocidade e precisão dos ensaios
* 12 - Nova aplicação para o Magician Lite
* 13 - Visitar os laboratórios do IPT
* 14 - Teste in loco (IPT) do MVP com amostras reais
* 15 - Acesso a impressoras 3D

## Oceano Azul

![image](https://user-images.githubusercontent.com/99221221/221012067-e4c738e2-1bcd-433f-8a77-9b477575add9.png)

**Aumentar**
* Precisão da análise
* Custo
* Velocidade
* Tecnologia
* Eficiência

**Diminuir**
* Mantenabilidade
* Robustez

**Criar**
* Parametrização
* Gasto energético

**Elimiar**
* Interveção humana

## Análise financeira

![image](https://user-images.githubusercontent.com/99221221/221013030-38d26f0c-d581-48ee-bd99-0469c0546937.png)

**Aspectos considerados:**
* Custo do Magnetum por ensaio (gasto energético + manutenção): R$ 2,125
* Custo do trabalhador por ensaio tradicional: R$ 7,81

Considerando que uso do tradicional custe e demore mais que do Magnetum e que a máquina fará uma jornada de trabalho de 6 horas todos os dias, enquanto o trabalhador fará uma de 8, estima-se que com 3000 usos, o equivalente a 168 dias, os gastos totais com o trabalhador supere o do Magnetum. 

## Proposta de Valor: Value Proposition Canvas

![image](https://user-images.githubusercontent.com/99221221/221010689-70564924-dd1f-4ee7-84db-0faa57005949.png)

## Personas

![image](https://user-images.githubusercontent.com/99221221/221011051-d283f015-dc3d-49fe-9435-14929ac38111.png)


## Histórias dos usuários (user stories)

**Épico: Como técnico, quero separar o material magnético de uma amostra com alta precisão e de modo automatizado para otimizar meu tempo e a qualidade da operação**
* Como técnico, quero acionar o início do ensaio por meio de um botão, após preparar a amostra nas bandejas, para que ele se realiza sem intervenção
* Como técnico, quero parametrizar as variáveis envolvidas no ensaio, como velocidade de passagem, intensidade magnética e distância, para analisar os resultados de forma precisa em diferentes condições
* Como técnico, quero ser alertado que o ensaio terminou por meio de sinal sonoro para que possa me concentrar em outras tarefas durante a execução do processo
* Como técnico, quero que o ensaio finalize automaticamente quando o ímã não atrair mais quantidade significativa de material magnético
* Como técnico, quero que o braço mecânico passe em cada bandeja para que realize coleta, limpeza e despejo dos materiais.
* Como técnico, quero que o sistema mantenha a distância e intensidade magnéticas constantes para que os resultados sejam precisos e confiáveis

**Épico: Como técnico, quero acessar relatórios precisos e padronizados de cada ensaio para analisar os resultados, filtrar dados e chegar a conclusões empiricamente embasadas.**
* Como técnico, quero ter um histórico das separações magnéticas que fiz para que possa consultar futuramente.
* Como técnico, quero que tenha filtros de busca por data de realização e por material para que consiga consultar com maior facilidade.

# Arquitetura do Sistema

## Diagrama geral
![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/Arquitetura%20Do%20Sistema/DiagramaDaSolucao.png?raw=true)

**Legenda do Diagrama**

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/Arquitetura%20Do%20Sistema/LegendaDoDiagrama.png?raw=true)

## Projeto mecânico
O projeto mecânico para nossa solução envolve dois módulos: um invólucro resistente à água na ponta do braço robótico, protegendo os imãs, e uma case simples para o circuito principal, incluindo Raspberry, placa e pontes H, a ser posicionada na traseira do robô. As conexões por fio serão organizadas ao longo do corpo do robô utilizando fixadores como fita adesiva, a fim de diminuir o risco de nós, curto-circuito ou qualquer outro dano à integridade eletrônica do projeto.

**Visão Superior**

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/Arquitetura%20Do%20Sistema/CroquiVisaoSuperior.png?raw=true)

O suporte para PCB será produzido em polímero, como o plástico ABS, através de impressão 3D. Escolhemos esse material por sua durabilidade, facilidade de processamento e baixo custo. Essas características são importantes para oferecer uma solução robusta, capaz de suportar choques mecânicos simples a um reduzido investimento inicial. Ademais, por não ser transparente, cumpre a tarefa de ocultar o circuito de vista, otimizando a experiência do usuário. Por fim, como essa case não entrará em contato direto com a água, não é necessário total impermeabilidade, viabilizando o uso da impressão 3D.

O case terá as dimensões 12 cm x 12 cm x 5 cm e será posicionado logo atrás do braço robótico. Caso a produção desse artefato não seja possível por falta de tempo ou acesso à infraestrutura necessária, pretendemos adquirir um case eletrônico IP65 online com dimensões semelhantes às desejadas.

**Visão Lateral**

O suporte para ímãs consiste em uma case octagonal, na qual serão fixados de dois a quatro ímãs. Por entrar em contato direto com a água, é essencial que o material de fabricação seja muito resistente a líquidos e, ao mesmo tempo, exerça interferência mínima no campo magnético. 

Não temos dimensões exatas ainda porque estamos testando a eficácia de dois, três ou quatro ímãs juntos, considerando o fluxo de corrente, campo magnético resultante e peso. Assim que chegarmos a uma conclusão nesse sentido, poderemos determinar o tamanho da case com propriedade.

Nesse sentido, nossa ideia principal é produzir a placa ortogonal em ABS através de impressão 3D, sob a qual os ímãs serão posicionados. Então, agregaremos uma capa de plástico flexível ou proteção rígida de acrílico sob a base dos eletroímãs para assegurar a resistência à água. Esse aspecto também permanece em aberto porque precisamos saber as dimensões finais para estimar o peso e, com isso, concluir qual opção afetará menos a performance do braço robótico.

Para os testes da Sprint 3, construímos um protótipo desse suporte utilizando papelão e fita adesiva, tendo 

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/Arquitetura%20Do%20Sistema/CroquiVisaoLateral.png?raw=true)


**Visão Robô**

A figura abaixo apresenta as dimensões do braço robótico Magician Lite, conforme especificações do fabricante.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/Arquitetura%20Do%20Sistema/CroquiRobo.png?raw=true)


## Projeto eletrônico

Como demonstrado na arquitetura da solução, o âmbito eletrônico do nosso projeto contempla, em visão geral, uma Raspberry Pi Pico W, eletroímãs e bombas d'água. A conexão entre esses componentes, por sua vez, é viabilizada através de reguladores de tensão e pontes H. Ressaltamos que, na esquemático e implementação do circuito da Sprint 3, utilizamos apenas quatro eletroímãs e duas bombas da água, conectados a duas pontes H, para prova de conceito. Futuramente, pretendemos agregar mais desses atuadores através de testes de eficácia e otimização.

###  Esquemático do circuito
![image](https://github.com/2023M5T2-Inteli/tectonics/blob/dev/media/Arquitetura%20Do%20Sistema/esquematicoDoCircuito.png?raw=true)

Conforme a figura, nosso circuito utiliza 10 pinos da Raspberry Pi Pico W, duas bombas d'água, quatro eletroímãs, duas pontes H e um regulador de tensão. Tudo isso é alimentado por uma fonte de 5V. 

Nesse contexto, o regulador de tensão é empregado para amplificar essa voltagem aos 12V necessários para o correto funcionamento dos eletroímãs. Desse modo, o componente recebe os 5V nas portas VCC IN/GND e envia 12V nas portas VCC OUT/GND. Estas, por sua vez, conectam-se diretamente à ponte H responsável por controlar os quatro eletroímãs. 

Nesta ponte H, conectamos dois ímãs de cada lado, em paralelo. Assim, pudemos controlar um par por vez através dos pinos de direção da ponte. Esses pinos foram ligados aos GPIOs 11, 12, 14 e 15 do microcontrolador, para que pudessem ser utilizados em PWM para variar a intensidade do campo magnético.

Já a segunda ponte H é alimentada diretamente pelos 5V e controla as duas bombas d'água. Não foi necessário utilizar o regulador de tensão nesta parte porque a especificação de voltagem das bombas é exatamente de 5V. Assim, conectamos os pinos de direção delas também a quatro GPIOs do microcontrolador (8, 9, 10, 11).

###  Implementação do circuito
A implementação do circuito se deu em uma placa perfurada de dimensão 12x18 cm, na qual foram soldados o microcontrolador e os fios de conexão entre componentes. Esses fios foram posicionados no lado inferior da placa por motivos estéticos. Ademais, por falta de suporte específico, ficaram apenas acoplados, através de jumpers soldados, as pontes H, o regulador de tensão, os eletroímãs e as bombas d'água. 

Nesse sentido, durante os testes, para minimizar riscos de curto-circuito e/ou contato com água, utilizamos fita isolante para proteger as soldas expostas, ampliamos os fios de conexão dos atuadores e prendemos essas conexões ao corpo do robô com fita adesiva.

Nas próximas sprints, pretendemos refatorar esse circuito, otimizando a organização da fiação e examinando a possibilidade de se produzir um PCB. Junto da case do projeto mecânico, o módulo eletrônico será muito mais resistente e de fácil manutenção.

#### Componentes utilizados
| Unidades | Nome | Link |
|------|-----------|-------|
| 2x  | Ponte H L298N     | [ datasheet ](https://files.comunidades.net/mutcom/Driver_Motor_ponteH__L298N.pdf)  |
| 1x| Regulador de Tensão Ajustável MT3608    | [ datasheet ](https://www.olimex.com/Products/Breadboarding/BB-PWR-3608/resources/MT3608.pdf)    |
| 1x| Raspberry Pi Pico W    | [ datasheet ](https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf)    |
| 4x| Eletroímã 12v    | [ compra ](https://produto.mercadolivre.com.br/MLB-1756894287-eletroim-12vdc-12v-5kg-forca-de-033a-_JM#position=12&search_layout=stack&type=item&tracking_id=f99d5a87-91f9-4bc5-bf67-01991f1188e0)    |
| 2x| Bomba d'água submersível Dc 3-5V 100l / H    | [ compra ](https://shopee.com.br/Bomba-D-'%C3%81gua-Submers%C3%ADvel-Pet-Mini-Dc3-5V-100l-H-Acess%C3%B3rios-Tanque-De-Peixes-Silenciosa-Para-Aqu%C3%A1rio-i.298167688.4751307098)    

#### Validação dos dispositivos eletrônicos

Os testes de validação de nosso circuito foram executados utilizando o mesmo código-fonte do teste de componentes. Nesse contexto, empregamos a interface gráfica da página "/demo" do frontend. Como esta seção trata dos dispositivos eletrônicos, relatamos apenas os testes referentes a essa parte do sistema (excluímos metas para braço robótico e feedback na interface gráfica).

| Componente                             | Entrada                                                       | Saída esperada                                                                   | Resultado do teste                                                                                                                                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Eletroímãs                              | Acionamento do botão de "ligar" na interface gráfica          | Emissão de campo eletromagnético nos ímãs, atraindo objetos magnéticos.            | Fracasso. Ao apertar o botão, os ímãs apresentaram forte tremor e não atraíram objetos magnéticos consistentemente. Materiais de maior massa foram particularmente difíceis de atrair, sendo necessário posicioná-los manualmente, sobre o ímã , assegurando contato direto, para se obter sucesso.                                                                                                                                                                         |
| Eletroímãs                              | Acionamento do botão de "desligar" na interface gráfica       | Cessão da emissão de campo eletromagnético, soltando quaisquer objetos captados. | Fracasso. Ao apertar o botão, os ímãs não soltaram os materiais captados consistemente. Isso ocorreu especialmente com objetos de menor massa, que permaneceram fixados à base dos ímãs mesmo após seu desligamento. Para soltá-los, foi necessário movê-los manualmente.                                                                                                                                                         |
| Bombas d'água                           | Acionamento do botão de "ligar" bombas d'água na interface gráfica            | Ativação das bombas em um dos sentidos de rotação.                                 | Sucesso. As bombas ativaram-se corretamente.                                                                                                                                                                                                           |
| Bombas d'água                           | Acionamento do botão de "ligar" bombas d'água na interface gráfica            | Desligamento das bombas                                  | Sucesso. As bombas desativaram-se corretamente.                                                                                                                                                                                                           |
| Acionamento dos eletroímãs na rotina integrada                          | Braço robótico posicionado sobre ou entre a primeira e segunda bandejas       | Emissão de campo eletromagnético nos ímãs, atraindo objetos magnéticos.                                 | Fracasso. Apesar dos ímãs ativarem-se nos período desejado, eles não apresentaram campo magnético suficiente para atrair materiais consistentemente. Também apresentaram forte tremor.                                                                                                                                                                                                         |
| Desligamento dos eletroímãs na rotina integrada                          | Braço robótico posicionado sobre a terceira bandeja            | Cessão da emissão de campo eletromagnético, soltando quaisquer objetos captados.                                 | Fracasso. Embora os ímãs tenham sido desativados, objetos de menor massa continuaram fixados à base dos atuadores, sendo preciso removê-los manualemente.                                                                                                                                                                                                           |
| Acionamento das bombas d'água na rotina integrada                          | Braço robótico posicionado sobre a segunda bandeja            | Ativação das bombas em um dos sentidos de rotação.                                 | Sucesso. As bombas ativaram-se corretamente.                                                                                                                                                                                                           |
| Desligamento das bombas d'água na rotina integrada                          | Braço robótico posicionado fora da segunda bandeja            | Desligamento das bombas em um dos sentidos de rotação.                                 | Sucesso. As bombas desativaram-se corretamente.                                                                                                                                                                                                           |
                                                       
**Considerações sobre eletroímãs:** O fracasso obtido nos testes com quatro ímãs foi inesperado, pois a validação de um único ímã havia funcionado perfeitamente. Frente ao problema, nossa primeira hipótese foi que houvesse um erro de código, conexão física, ou interferência entre os campos magnéticos. 

Entretanto, ao examinar a voltagem em diferentes pontos do circuito utilizando um voltímetro, descobrimos que, apesar de a ponte H receber 12V do regulador de tensão, ela está enviando apenas 0,65V-0,75V para os ímãs. Logo, acreditamos ser um problema de divisão de corrente dentro do componente. 

Portanto, na Sprint 4, pretendemos testar a troca da ponte H e, se isso não funcionar, a diminuição do número de eletroímãs por ponte.


O teste de integração pode ser visto [neste link](https://drive.google.com/file/d/1cPIdNrdqBF0necSuE6qcQWNYOLx2EU66/view?usp=sharing).

## Módulos do Sistema e Visão Geral (Big Picture)

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/Arquitetura%20Do%20Sistema/Tabela1.png?raw=true)

## Descrição dos Subsistemas

### Descrição dos componentes

![image](https://raw.githubusercontent.com/2023M5T2-Inteli/tectonics/main/media/Arquitetura%20Do%20Sistema/TabelaDeFun%C3%A7%C3%B5es.png)



## Tecnologias Utilizadas
### Testes de componentes
#### Movimentação do robô

A movimentação do robô foi testada em três etapas. Inicialmente, fizemos uma exploração das funcionalidades do Magician Lite com o auxílio do software de controle Dobot Studio. Nesse momento, utilizamos os controles manuais da plataforma para nos familiarizarmos com os de periféricos disponíveis, como a garra, a sucção e a caneta. Com isso, também aprendemos mais sobre os limites físicos do robô, no que tange a envelope de trabalho em diferentes configurações das articulações. 

Começando a testar as funcionalidades de programação do robô, configuramos o desenho de um vetor de alta complexidade. Para isso, seguimos os seguintes passos:

1. Fizemos o download do [vetor desejado](https://drive.google.com/file/d/1btHzWGOxXzzZMx91I4lkRq3Hw46jGhcT/view?usp=sharing
) (em svg)
1. Conectamos o robô à fonte e ao computador via USB
2. Trocamos a ponta do robô pelo suporte de caneta
3. Posicionamos um caderno A3 horizontalmente à frente do robô, sob a ponta
4. Calibramos a altura manualmente, utilizando os controles do software, para que a ponta da caneta trocasse o papel
5. Acessamos a seção de "Write & Draw" do Dobot Studio
6. Importamos o vetor na área de configuração de desenho
7. Redimensionamos e reposicionamos o vetor para que ela ficasse contida nos limites do caderno
8. Pressionamos o botão 'AutoZ' para desativá-lo. Isso evita que o robô modifique a altura da caneta, que foi calibrada no passo 4
9.  Pressionamos o botão 'Start'

A execução do desenho levou em torno de 10 minutos. Um vídeo acompanhando o processo se encontra abaixo.

[Teste de desenho](https://drive.google.com/file/d/1DKwGRYJMMwX0WrUkw78yCvqYAucw6ZM4/view?usp=share_link)

Na segunda etapa, objetivamos movimentar o robô diretamente por scripts em Python. Para isso, seguimos os seguintes passos:

1. Instalamos a biblioteca (API) de comunicação Pydobot através de 'pip install pydobot'
2. Conectamos o robô à fonte e ao computador via USB
3. Descobrimos qual porta estava conectada ao robô através de tentativa e erro na interface do Dobot Studio. Isso foi feito apertando o botão "Conectar" para cada opção de porta até que a conexão fosse bem-sucedida.
4. Utilizamos um código de exemplo de movimentação simples, trocando o argumento de porta pela porta encontrada na etapa 3 (no caso, 'COM7')

```
from serial.tools import list_ports

import pydobot

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = 'COM7'

device = pydobot.Dobot(port=port, verbose=True)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

device.move_to(x + 20, y, z, r, wait=False)
device.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing

device.close()
```

5. Executamos o código

O teste foi bem-sucedido e o robô se movimentou conforme esperado. A partir daí, passamos algum tempo testando diferentes argumentos e operações algébricas na função move_to(). Nesse momento, descobrimos que os limites de envelope de trabalho também se aplicam a essa função, de modo que, quando o robô está posicionado em certos pontos, ele é incapaz de se movimentar para alguns outros pontos específicos. 

Posteriormente, mapeamos as coordenadas desejadas para a movimentação do robô sobre as três bandejas, almejando quatro posições em cada: duas altas e duas baixas. Como os valores de altura e de rotação eram constates, também os substituímos por variáveis. Ademais, adicionamos "pontos de volta" no final do ciclo, correspondentes ao ponto alto final das bandejas 2 e 3, para facilitar a volta do robô. Sem eles, o braço travaria devido às limitações do envelope de trabalho. Este foi o array resultante:

```
high_height = 70
low_height = -32
rotation = -86

tray_coordinates = [
    # BANDEJA 1
    (35, -248, high_height, rotation), # Ponto alto inicial
    (35, -248, low_height, rotation), # Ponto baixo inicial
    (216, -248, low_height, rotation), # Ponto baixo final
    (216, -248, high_height, rotation), # Ponto alto final

    # BANDEJA 2
    (263, -112, high_height, rotation), # Ponto alto inicial
    (263, -112, low_height, rotation), # Ponto baixo inicial
    (263, 68, low_height, rotation), # Ponto baixo final
    (263, 68, high_height, rotation), # Ponto alto final

    # BANDEJA 3
    (222, 255, high_height, rotation), # Ponto alto inicial
    (222, 255, low_height, rotation), # Ponto baixo inicial
    (19, 255, low_height, rotation), # Ponto baixo final
    (19, 255, high_height, rotation), # Ponto alto final

    # PONTOS INTERMEDIÁRIOS PARA REINICIAR
    (222, 255, high_height, rotation), # Ponto alto inicial da bandeja 3
    (216, -248, high_height, rotation) # Ponto alto inicial da bandeja 2
]
```

Então, juntamos esse array com um código de execução básico:

```
for coordinate in tray_coordinates: 
  device.move_to(*coordinate, wait=True)
```

Rodando tudo isso, conseguimos fazer o braço se movimentar uma vez sobre cada bandeja, conforme vídeo abaixo.

[Movimentação simples](https://drive.google.com/file/d/1U_hwCO9obIUuMkyjYx5wSZpOMIPoqCgo/view?usp=share_link)

Por fim, iniciamos a implementação um servidor simples em Flask para automatizar uma movimentação específica através de uma interface gráfica web. Para isso, fizemos uma rota GET que, quando requisitada, executa a função de movimentação do robô. Este código, por ser muito extenso, está disponível na pasta src deste repositório git. Como ainda não foi completamente desenvolvido, não há vídeos mostrando seu funcionamento integral. Isso é uma meta para a Sprint 3.

#### Eletroímã na ponte H

Um dos fatores fundamentais em nosso projeto é o uso de um eletroímã acoplado ao braço robótico. Com ele, será possível não só ativar e desativar o campo magnético, permitindo a programação da captura e despejo de partículas magnéticas, como também será possível varial a intensidade do campo produzido a fim de atrair diferentes categorias de material.

Nesse sentido, inicialmente testamos um eletroímã diretamente na fonte de 12V (a voltagem máxima do eletroímã). Como esperado, ele foi capaz de atrair uma moeda de dez centavos quando ligado na fonte e a soltou quando o desconectamos. Tendo esse conhecimentos, passamos a estudar a integração do ímã com o Raspberry Pi Pico W. A dificuldade, nesse momento, era alimentar uma voltagem variável ao ímã superior à voltagem disponível no VCC do microcontrolador (3V3).

Para solucionar isso, conectamos o ímã a uma ponte H. Dessa forma, pudemos alimentar a ponte continuamente com os 12V enquanto controlávamos o estado (ativado/desativado) do ímã através dos pinos de direção da ponte, responsáveis por inverter a polaridade da voltagem. Seguindo a lógica de ponte H, para que o ímã ligasse, apenas um pino deveria estar ativo. Com ambos ligados ou desligados, o ímã permanecia desativado. Nesse contexto, os pinos foram conectados a pinos de output do Raspberry, de modo que o microcontrolador decidisse, através de sinais binários, quais pinos da ponte H deveriam ser ativados. Ademais, a entrada positiva da ponte H foi conectada diretamente à fonte, enquando a entrada negativa foi conectada em paralelo à saída negativa da fonte e do GND do Raspberry.

Feita essa configuração de hardware, iniciamos os testes com código. Pensando apenas no comportamento binário, construímos um programa simples que envia sinal de HIGH para apenas um pino na função de ligar o ímã, e mandava sinais de LOW para ambos os pinos na função de desligar o ímã. O código está disponível abaixo.


```
import machine

magnet_pin_1 = machine.Pin(16, machine.Pin.OUT)
magnet_pin_2 = machine.Pin(15, machine.Pin.OUT)

def enable_magnet():
    magnet_pin_1.value(1)
    magnet_pin_2.value(0)

def disable_magnet():
    magnet_pin_1.value(0)
    magnet_pin_2.value(0)

```

Então, chamamos cada função separadamente em diversas execuções. O resultado foi conforme o esperado.

O próximo passo foi dinamizar a intensidade do ímã. O método utilizado para esse fim foi o PWM (Pulse Width Modulation). Ele consiste em alternar rapidamente a tensão aplicada ao dispositivo entre níveis altos e baixos em um determinado ciclo de tempo, conhecido como período. Ao variar a largura dos pulsos (ou seja, a quantidade de tempo que a tensão é mantida alta em relação ao período), é possível controlar a tensão média aplicada ao dispositivo. Por exemplo, se a tensão é alternada entre 0V e 12V com uma frequência de 1kHz e uma largura de pulso de 50%, a tensão média aplicada seria de 6V.

Nesse sentido, para atingir a intensidade magnética de qualquer voltagem abaixo de 12V, bastaria enviar uma largura de pulso proporcional à fração de voltagem desejada. Felizmente, o Micropython, linguagem utilizada para programar o Raspberry Pi Pico W, possui um método nativo para PWM. Nosso código, então, começava com a declaração dos pinos como pinos PWM, em vez de apenas pinos binários. Também definimos a frequência como 1kHz, como valor de teste.

```
import machine

magnet_pin_1 = machine.PWM(machine.Pin(16, machine.Pin.OUT))
magnet_pin_2 = machine.PWM(machine.Pin(15, machine.Pin.OUT))

magnet_pin_1.freq(1000)
magnet_pin_2.freq(1000)

```
Depois, atualizamos as funções de ligar e desligar o ímã. Nessa primeira, adicionamos um argumento de voltagem desejadas e aplicamos o método PWM.duty_u16() para definir a largura de pulso a ser enviada ao pino. Um ponto importante nesta etapa é que a unidade desse argumento não deveria ser passada na porcentagem escolhida (50%, por exemplo), e sim no valor proporcional no intervalo 0 a 65535. Logo, tivemos de converter a voltagem desejada para a fração dessa escala em cada chamada da função de duty_u16(). A função de desligar, por sua vez, passava 0 como argumentos para ambos os pinos.

```

def enable_magnet(voltage):
    magnet_pin_2.duty_u16(0)
    magnet_pin_1.duty_u16(int(voltage / 12.0 * 65535))

def disable_magnet():
    magnet_pin_1.duty_u16(0)
    magnet_pin_2.duty_u16(0)

```
Executando essas funções com diferentes voltagens, atingimos o comportamento esperado, com a intensidade da atração entre o ímã e os materias magnéticos de teste variando conforme aumentávamos e diminuíamos o argumento de voltagem.

Feito isso, adicionamos rotas no servidor e um botão no frontend para controlar o liga e desliga do ímã, ainda sem variação da voltagem. Este código está disponível na pasta src deste repositório git, por ser muito extenso para adicionar aqui. Dito isso, o vídeo abaixo demonstra seu funcionamento:

[Ímã ligando e desligando no front](https://drive.google.com/file/d/1tNGGaVWdjG-uf2RkJPIhACx0uDh1AWXc/view?usp=share_link)

Por fim, voltando ao código de movimentação do robô visto no final do teste anterior, adicionamos uma linha que ativava a sucção da ponta. 

```
device.suck(True)
for coordinate in tray_coordinates: 
  device.move_to(*coordinate, wait=True)
```

Com isso, pudemos conectar o ímã ao movimento braço robótico:

[Ímã conectado ao braço](https://drive.google.com/file/d/1nGkIPEVVNb14Duce5NOnQtC0NVbb49da/view?usp=share_link)


#### Bomba d'água na ponte H

Similarmente ao eletroímã, a bomba d'água também requereu o uso do ponte H por exigir voltagem acima de 3V3. Ainda assim, inicialmente, fizemos um teste conectando-a diretamente a fonte em 12V. Como esperado, ela foi ativada e movimentou a água significativamente.

[Bomba d'água na fonte](https://drive.google.com/file/d/1jfaO7tCQ4pp-55x3oSPvWAU1O0QgRn3F/view?usp=share_link)

Depois, conectamos a bomba à ponte H e ligamos os pinos de sentido restantes a dois pinos digitais livres do Raspberry. Implementamos, então, funções de ligar e desligar, semelhantemente ao primeiro código utilizado para o eletroímã. Nesse caso, o pino ativado influencia no sentido de rotação da bomba. Ainda assim, como esse sentido não influencia no objetivo do uso da bomba (movimentar a água para dispersar material e lavar impurezas), pode-se ativar qualquer um dos pinos. Semelhante, como não é necessário alterar a intensidade da bomba, não tivemos que trabalhar PWM neste teste.


```
import machine

pump_pin_1 = machine.Pin(16, machine.Pin.OUT)
pump_pin_2 = machine.Pin(15, machine.Pin.OUT)

def enable_pump():
    pump_pin_1.value(1)
    pump_pin_2.value(0)

def disable_pump():
    pump_pin_1.value(0)
    pump_pin_2.value(0)

```

O teste unitário de cada função foi bem-sucedido. Então, conectamos essas funções também a rotas de servidor e um botão na interface gráfica, conforme descrito na pasta src deste repositório git. O vídeo abaixo sumariza o funcionamento final dos componentes da ponte H integrados ao frontend:

[Componentes integrados](https://drive.google.com/file/d/1iMuU_Au-HOIZtkMis8Z6_jKLUNROaPFZ/view?usp=sharing)


#### Sensor de campo eletromagnético

Um dos objetivos deste projeto é estimar o peso do material magnético captado pelo eletroímã sem depender da secagem do mesmo. Nossa ideia inicial para isso foi acoplar um sensor magnético atrás do eletroímã, a fim de aproximar o peso da amostra através das variações no campo magnético conforme mais material fosse captado. 

Para testar essa hipótese, utilizamos um sensor de efeito hall KY-024 em um circuito simples. Esse circuito continha um LED de feedback, que brilharia quando o sensor captasse campo magnético. Assim, nesse primeiro teste, o comportamento esperado era binário, informando apenas se havia algum campo significativo na região.

Um esquemático do circuito do sensor pode ser visto abaixo. O capacitor, em cinza, não foi utilizado, e o LED foi conectado separadamente, em outra porta do Raspberry, e controlado apenas por código.

![image](https://raw.githubusercontent.com/2023M5T2-Inteli/tectonics/main/media/testes_de_componentes/sensor_campo_magnetico/hall_effect_sensor_circuit.png)

O código, por sua vez, foi o seguinte:

```
import machine
led = machine.Pin(18, machine.Pin.OUT)
sensor = machine.Pin(14, machine.Pin.IN)

while True:
    if(sensor.value() == 1):
        led.HIGH()
    else:
        led.LOW()
```

O funcionamento pode ser visto no vídeo abaixo:

[Sensor de campo eletromagnético](https://drive.google.com/file/d/1ZvMhhsyrQqPlQ1OZxav6_Ht2Wmu-avOB/view?usp=share_link)

Posteriormente, refatoramos esse código para que ele lesse valores analógicos, a fim de examinar as variações no campo perante a quantidade de material atraído pelo ímã. Para isso, trocamos o tipo de pino por ADC e utilizamos a função read_u16.

```
import machine
sensor = machine.ADC(28)

while True:
    print(sensor.read_u16())
    time.sleep(0.1)
```

Infelizmente, neste teste, as leituras obtidas se concentravam em três intervalos muito distantes entre si: quando o ímã estava desligado, o console exibia leituras em torno de 800; com o ímã a média distância, líamos 20.000 a 27.000; por fim, com o ímã muito perto, tínhamos 64.000-65.000. O vídeo abaixo exibe o comportamento errático.

[Leituras do sensor](https://drive.google.com/file/d/1FX70Vs9eu51dPvugF0spTe9vWaQVk8CA/view?usp=sharing)

De todo, esses saltos eram bruscos e não representavam as microvariações que pretendíamos analisar. Com isso, percebemos que esse sensor não atenderá nossos objetivos. Concluímos, portanto, ser de fato necessário utilizar a célula de carga para estimar o peso da amostra.

#### Célula de carga e amplificador HX711

A célula de carga converte uma força em um sinal elétrico que pode ser medido. Este sinal irá mudar proporcionalmente à força aplicada. A células de carga é composta por uma barra de metal com extensômetros fixados. Os extensômetros são sensores elétricos que medem força ou tensão em um objeto. Quando uma força externa é aplicada a um objeto, como a barra de metal, ocorre uma deformação em sua forma, o que faz com que a resistência dos extensômetros varie. A mudança na resistência é proporcional à carga aplicada, permitindo-nos calcular o peso dos objetos.

Sabe-se que existem alterações de tensão, todavia, como essas mudanças são muito pequenas, é necessário um amplificador. O amplificador utilizado se chama HX711 e se comunica com o microcontrolador utilizando de uma interfaze de dois fios, "Clock" e "Data". Para realizar o teste foi preciso prender a célula de carga de maneira a criar uma tensão entre as extremidades opostas da barra de metal. 

![image](https://raw.githubusercontent.com/2023M5T2-Inteli/tectonics/main/media/testes_de_componentes/celula_de_carga/c%C3%A9lula_de_carga_entre_placas.png)

Após isso, foram feitas as seguintes ligações:

![image](https://raw.githubusercontent.com/2023M5T2-Inteli/tectonics/main/media/testes_de_componentes/celula_de_carga/conexoes_celula_de_carga.png)

O teste consistiu em duas etapas: a calibração da célula e a medição de peso de objetos previamente conhecidos. A primeira etapa é crucial para o teste, pois é a partir dela que determinamos o fator de calibração, que pode ser obtido dividindo o valor lido pela célula pelo peso já conhecido. A segunda etapa consistiu na medição real dos objetos, utilizando o fator de calibração obtido na primeira etapa.

O código em sua íntegra está disponível em src/embedded/weight_cell. Não foi colocado neste relatório por ser muito extenso. Ainda assim, o vídeo abaixo demonstra o funcionalmento final.

[Vídeo do teste realizado](https://drive.google.com/file/d/19G_qC6mr0JAeuuYVfvO6fVKM8mR57QWV/view?usp=share_link)

Isso tudo foi testado em um ESP-32 com C++. Pretendemos adaptar essa funcionalidade para o Raspberry Pi Pico W com Micropython, integrando isso ao resto do sistema, na Sprint 3.

### Relatório de entradas e saídas dos testes

| Componente                             | Entrada                                                       | Saída esperada                                                                   | Resultado do teste                                                                                                                                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Braço robótico                         | Acionamento do botão de início do ensaio na interface gráfica | Movimentação do robô segundo as coordenadas de posição programadas para o ensaio (quatro pontos sobre cada bandeja: ponto alto inicial, ponto baixo inicial, ponto baixo final e ponto alto final) | Sucesso. Robô se movimentou conforme o esperado.                                                                                                                                                                                                   |
| Eletroímã                              | Acionamento do botão de "ligar" na interface gráfica          | Emissão de campo eletromagnético no ímã, atraindo objetos magnéticos.            | Sucesso. Ao apertar o botão, o ímã atraiu uma moeda de dez centavos.                                                                                                                                                                               |
| Eletroímã                              | Acionamento do botão de "desligar" na interface gráfica       | Cessão da emissão de campo eletromagnético, soltando quaisquer objetos captados. | Sucesso. Ao apertar o botão, o ímã soltou a moeda e parou de atrair materiais magnéticos.                                                                                                                                                          |
| Sensor de campo eletromagnético        | Aproximação de campo magnético                                | Iluminação do LED de feedback                                                    | Sucesso. Ao aproximar o ímã ligado, o LED acendeu.                                                                                                                                                                                                 |
| Sensor de campo eletromagnético        | Afastamento de campo magnético                                | Apagamento do LED de feedback                                                    | Sucesso. Ao afastar ou desligar o ímã, o LED se apagou.                                                                                                                                                                                            |
| Sensor de campo eletromagnético analógico     | Aproximação de campo magnético                                | Aumento gradual e granular do valor das leituras                                                    | Fracasso. Leituras passaram do intervalo de 800-900 para 20.000-27.000 e depois 64.000-65.0000.                                                                                                                                                                                            |
| Sensor de campo eletromagnético analógico     | Afastamento de campo magnético                                | Diiminuição gradual e granular do valor das leituras                                                    | Fracasso. Leituras passaram do intervalo de 64.000-65.0000 para 20.000-27.000 e depois 800-900.                                                                                                                                                                                            |
| Célula de carga e amplificador         | Adição de massa sobre a placa da célula de carga              | Exibição do peso da massa adicionada no console do microcontrolador              | Sucesso. A adição de um case de fone de ouvido foi reconhecida e corretamente pesada pela célula de carga. A acuracidade foi estimada através da comparação do peso calculado pela célula de carga com o peso calculado por uma balança calibrada. |
| Bomba d'água                           | Conexão da bomba d'água, na ponte H, à fonte em 5V            | Ativação da bomba em um dos sentidos de rotação.                                 | Sucesso. A bomba ativou-se corretamente.                                                                                                                                                                                                           |
| Contagem de ciclos (interface gráfica) | Repetição dos ciclos (passadas) do robô em um mesmo ensaio    | Atualização do número de ciclos (passadas) no frontend.                          | Sucesso. A linha de contagem de ciclos mudou conforme o esperado.                                                                                                                                                                                  |
| Contagem de ciclos (interface gráfica) | Finalização de um ensaio                                      | Reset da contagem de ciclos, voltando ao 0.                                      | Sucesso. Ao terminar um ensaio, assim que o robô parava de se movimentar, o contador voltava a 0.                                                                                                                                                  |



# UX e UI Design

Na Sprint 3, implementamos as principais telas da interface gráfica e ampliamos a integração da página "/demo" para testes. Na Sprint 4, pretendemos integrar o as telas oficiais, isto é, as implementadas na Sprint 3 com base no design do Figma, com o resto do sistema.

Como linha geral, priorizamos elementos minimalistas, intuitivos e de fácil entendimento. Seguindo o estilo utilizado até agora nos slides e logotipos, apostamos em uma paleta de cores com alto contraste e foco em tons de roxo. 

A interface oficial apresenta uma sidebar simples, com tela inicial, histórico de relatórios, perfil e link temporário à página de demo. A tela principal, por sua vez, traz um botão de destaque para iniciar um ciclo, assim como campos de preenchimento de mais informações para cada execução. Clicando na seta na base da página, pode-se visualizar um card na qual serão disponibilizadas mais detalhes sobre o ensaio. O template dessas informações será implementado na Sprint 4.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/dev/media/interface_grafica/home1.png?raw=true)

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/dev/media/interface_grafica/home2.png?raw=true)

Já na aba de histórico, tem-se ensaios antigos com diversas funcionalidades de filtragem. Futuramente, objetivamos adicionar opções de compilação, exportação e compartilhamento também.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/dev/media/interface_grafica/history1.png?raw=true)

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/dev/media/interface_grafica/history2.png?raw=true)

Por fim, a página de perfil permanece em construção.

O design inicial do Figma pode ser conferido [aqui](https://www.figma.com/file/6mBFBLaAB9pjVo9Z3GzauB/Magnetum?node-id=23%3A2&t=tj4cyeV3llJXr2hb-1). Para a interface de testes, utilizamos um design simples, com um único vetor em tons de verde para decoração na base da página.

![image](https://github.com/2023M5T2-Inteli/tectonics/blob/main/media/interface_grafica/interface_demo.png)

# Projeto de Banco de Dados

## Modelo Conceitual

## Modelo Lógico

# Teste de Software

## Testes Unitários


## Teste de Usabilidade


# Análise de Dados


# Manuais

## Manual de Implantação

## Manual do Usuário

## Manual do Administrador


# Referências

[Random Nerd Tutorials](https://randomnerdtutorials.com/esp32-load-cell-hx711/)
