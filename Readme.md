![Logo do Projeto](./assets/Logo.jpeg)

# 🏛️ IntegraTur: Solução para Gestão Integrada das Secretarias de Turismo e Cultura de Recife  

**Projeto desenvolvido para a Prefeitura do Recife, visando a integração entre as Secretarias de Turismo e Cultura.**  

---

## 👥 Equipe  
| Nome             | Funções | Hobby                                                                 | Contato |
|------------------|---------|-----------------------------------------------------------------------|---------|
| André Ferraz     | Scrum Master| Surfar, ir à academia, jogar basquete e acompanhar outros esportes.  |afg@cesar.school     |
| Luiz Felipe      |Project Owner| Jogar videogame, cozinhar e jogar vôlei.                             | lfmf@cesar.school      |
| Gustavo Rodrigues|Quality Assurance (QA)| Escutar música, ir à academia e andar de bicicleta.                  | grq@cesar.school     |
| Jorge Tadeu      |Desenvolverdor Front End| Ir à academia e jogar vôlei.                                         |jtgsf@cesar.school     |
| Maria Eduarda    |Desenvolverdor Front End| Escutar música, jogar videogame, pintar e desenhar.                  | merm@cesar.school    |
| Maria Julia      |Desenvolverdor Front End| Desenhar (papel e digital, ainda aprendendo), ler e assistir sitcom. | mjmr@cesar.school     |
| Mateus Jose      |Desenvolverdor Back End| Jogar videogame, praticar natação, correr e acompanhar esportes.     | mjgmg@cesar.school     |
| Matheus Melquiades |Desenvolverdor Front End| Jogar videogame, ler quadrinhos e ir ao cinema.                      | mmn3@cesar.school     |
  
---

## 📌 Contexto do Problema  
As secretarias municipais de **Turismo** e **Cultura** de Recife enfrentam desafios críticos devido à **falta de comunicação e integração**, resultando em:  
- **Ações desarticuladas** e perda de eficiência.  
- **Retrabalho** e custos desnecessários.  
- **Impacto negativo** na experiência do cidadão e turistas.  

A Prefeitura do Recife nos solicitou uma solução para **conectar essas áreas**, otimizando recursos e melhorando serviços públicos.  

---

## 🎯 Objetivo do Produto  
O **IntegraTur** é um sistema que:  
✔ **Centraliza informações** entre as secretarias.    
✔ **Reduz duplicidade** de esforços e custos operacionais.  
✔ **Melhora a experiência** do usuário

## 📋 Histórias de Usuário Implementadas

### 1. Etapa de chat de Secretarias  
**Link:** https://integratur.atlassian.net/browse/INT-7?atlOrigin=eyJpIjoiNTc1ODRlYTEyOGM4NDZjNDg2MjE5YTJjM2ZhYWM4N2UiLCJwIjoiaiJ9

**Descrição:**  
“Como Diretora de Comunicação da Prefeitura, quero me conectar com as Secretarias via chat, para resolver questões dos eventos.”  

**Conversa com o PO:**

"Nessa história, o usuário deverá ter ferramentas para se comunicar via chat com os demais membros da secretaria podendo conversar tanto de forma privada com um determinado membro, quanto a criação de um grupo para adicionar membros que irão organizar o mesmo evento".

**Critérios de aceitação (CDA):**  
- É necessário que a ferramenta tenha uma parte para conversas entre membros de ambas as secretarias.  
- A página de chat deve conter receber somente digitação, não possibilitando, inicialmente, o envio de áudio.  
- A aba deve ter uma restrição para palavras consideradas ofensivas.  

**Prioridade:** Média.  
**Estimativa de Esforço:** 5 horas.  

---

### 2. Cadastrar Evento  
**Link:** https://integratur.atlassian.net/browse/INT-3?atlOrigin=eyJpIjoiMTk5NWQzMWQ4MWZmNGI1MGE1MzBkZWRiZDA0MWZiZmIiLCJwIjoiaiJ9

**Descrição:**  
"Como gestor da Secretaria de Turismo, quero cadastrar eventos no calendário compartilhado para garantir que as atividades sejam planejadas sem conflitos e divulgadas adequadamente."

**Conversa com o PO:**

"O usuário deve ser capaz de cadastrar eventos em um calendário compartilhado para facilitar a visualização e programar eventos de forma mais dinâmica através de uma única tela que mostra eventos sendo produzidos em um ou mais meses para cadastrar o evento o usuário deverá ser capaz de adicionar título no evento, data, atrações, programação, local, atualizar o calendário em tempo real com a criação de outros eventos, amostragem de recursos como fornecedores patrocinadores e equipamento na hora de cadastrar o evento, requisitos como alvarás e licenciamentos e mensagem de que o evento foi adicionado ao usuário terminar de cadastrar e clicar em adicionar".

**Critérios de Aceitação (CDA):**  
- Título do evento  
- Data  
- Atrações e orçamento  
- Programação  
- Local (com opção de selecionar endereços pré-cadastrados).  
- Exibir mensagem de sucesso: "Evento 'Carnaval 2025' cadastrado com sucesso!"  
- Atualizar o calendário em tempo real.  
- Recursos como fornecedores, patrocinadores e equipamentos  
- Requisitos como alvarás, licenças e autorizações  

**Prioridade:** Alta  
**Estimativa:** 5 horas  .

---

### 3. Procurar Evento
**Link:** https://integratur.atlassian.net/browse/INT-4?atlOrigin=eyJpIjoiM2JjNzE0OTNmZWY5NGI1MjhhYjJjMDM4OGJkNWE4NzUiLCJwIjoiaiJ9

**Descrição:**  
"Como funcionário da Secretaria de Turismo ou Cultura, quero buscar eventos por palavras-chave ou pelo nome do mesmo para que eu tenha um acesso mais ágil ao card do evento através do feed". 

**Conversa com o PO:**

"O usuário, deverá ter ferramentas capazes de buscar eventos na home com base em palavras chaves inseridas por um usuário em uma box, como o  nome do evento e exibir mensagem caso nenhum evento seja encontrado com as palavras chaves citadas".

**Critérios de Aceitação (CDA):**  
- Barra de busca fixa no topo da home: "Buscar por nome, data ou local...".   
- Buscar por: Título do evento (ex.: Carnaval). Local (ex.: Praça Central).  
- Exibir mensagem "Nenhum evento encontrado" se a busca não retornou resultados.  
- Exibir o evento respectivo ao nome ou palavra pesquisada. 

**Prioridade:** Alta 
**Estimativa:** 4 horas  

---

### 4. Cadastro de Fornecedores  
**Link:** https://integratur.atlassian.net/browse/INT-10?atlOrigin=eyJpIjoiNTBjYWNkNDAwNzlkNGM3N2FlMzM3MjZlNDNlNTU3MWMiLCJwIjoiaiJ9

**Descrição:**  
"Como Secretário de Cultura, quero cadastrar fornecedores para facilitar a organização e logística dos eventos."  

**Conversa com o PO:**

"Nessa historia, o usuário deverá ter ferramentas necessárias para cadastrar fornecedores e prestadores de diversos serviços como iluminação, estrutura, marketing e etc... deverá ter um campo para adicionar à empresa, com o nome da mesma, o tipo de serviço que presta e o histórico de eventos produzidos para as secretarias, essa empresa deverá ser cadastrada em um banco de dados para que possam ser usadas novamente na elaboração de outros eventos".

**Critérios de Aceitação:**  
- Deve haver um campo para inserir o nome do fornecedor.  
- Deve ser possível adicionar informações de contato e tipo de serviço prestado.  
- O sistema deve permitir cadastrar múltiplos fornecedores.  
- Os fornecedores cadastrados devem ficar disponíveis para seleção em eventos futuros.  

**Prioridade:** Média  
**Estimativa de esforço:** 4 horas  

---

### 5. Login Institucional  
**Link:** https://integratur.atlassian.net/browse/INT-1?atlOrigin=eyJpIjoiYWVhNTRlNWYxY2Q3NDhmZjgxZjNhMzZhODY3NWQ4MmQiLCJwIjoiaiJ9

**Descrição:**  
“Como funcionário da Secretaria de Turismo, quero fazer login no Integratur usando meu e-mail institucional para acessar ferramentas exclusivas de planejamento e evitar acesso não autorizado”. 

**Conversa com o PO:**

"O requisito principal para um usuário logar e usar o email institucional, essa funcionalidade garante que apenas usuários da secretaria entrem na plataforma. Cada usuário deverá ter sua senha própria e caso seja a sua primeira entrada o usuário deverá clicar na primeira vez para criar seu cadastro com email institucional e criar sua própria senha para a plataforma".

**Critérios de aceitação:**  
- O sistema valida e-mails (institucionais) no formato @recife.pe.gov.br  
- Exibe mensagem de erro se e-mail/senha estiverem incorretos.  
- Redireciona para a página inicial após login válido.  

**Prioridade:** Alta  
**Estimativa de esforço:** 3 horas  

---

### 6. Calendário de Eventos  
**Link:** https://integratur.atlassian.net/browse/INT-5?atlOrigin=eyJpIjoiZmIzMmVhY2M3ZGNkNGJmOWE2ZDZhYjk3OGMxNzcxMGUiLCJwIjoiaiJ9

**Descrição:**  
"Como usuário, eu quero visualizar um calendário de eventos para acompanhar a programação de eventos de forma organizada."  

**Conversa com o PO:**

"O usuário deverá ser capaz de visualizar eventos que estão sendo produzidos no dia de determinado mês de forma organizada em formato de agenda, os eventos devem aparecer nos dias correspondentes da sua elaboração e mostrar o representante responsável, deve ser possível navegar entre os meses para ser possível ver eventos futuros, é possível navegar para ver eventos passados que já foram realizados com sucesso".

**Critérios de Aceitação:**  
- O calendário deve exibir os dias do mês em um formato organizado.  
- Os eventos cadastrados devem aparecer nos dias correspondentes.  
- Deve ser possível navegar entre os meses para visualizar eventos passados e futuros.  
- Os eventos devem ser destacados com um nome e um ícone representativo.  

**Prioridade:** Alta  
**Estimativa de esforço:** 5 horas  

---

### 7. Gestão de Orçamento  
**Link:** https://integratur.atlassian.net/browse/INT-9?atlOrigin=eyJpIjoiZjU3MzhkZDVhMzFmNDBjNjlhNDliMTUxNmQ5MjY1ZmYiLCJwIjoiaiJ9

**Descrição:**  
"Como gestor da Secretaria de Turismo ou Cultura, quero cadastrar e monitorar o orçamento total do evento, para manter o controle financeiro."  

**Conversa com o PO:**

"Neste campo, o usuário que preencherá durante a criação de um novo evento o orçamento total do evento, e conforme for preenchendo-o mostrar se está extrapolando ou não do valor estipulado, deverá haver um botão de adicionar despesas, barra de progresso caso esteja perto de passar do orçamento, permitir incluir ou excluir despesas, botão exportar para pdf com total gasto por categoria"

**Critérios de Aceitação (CDA):**  
- Campo para inserir valor total.  
- Exibir mensagem de confirmação: "Orçamento inicial salvo com sucesso!".  
- Descrição (ex.: "Aluguel de palco").  
- Botão "Adicionar Despesa" que atualiza o saldo em tempo real.  
- Barra de progresso ou gráfico mostrando: Verde: 0-80% do orçamento utilizado. Amarelo: 81-99% do orçamento. Vermelho: 100% ou mais (ex.: "Orçamento ultrapassado em R$ 1.200,00").  
- Permitir editar/excluir despesas mesmo após ultrapassar o orçamento.  
- Não bloquear o cadastro de novas despesas.  
- Botão "Exportar para PDF" com resumo: Total gasto por categoria.  

**Prioridade:** Alta  
**Estimativa:** 6 horas  

---

### 8. Filtro por Secretaria  
**Link:** https://integratur.atlassian.net/browse/INT-6?atlOrigin=eyJpIjoiNTVmYzY4MWY0MTkxNGZmZGFjNDI0MDE0ODcwMmU5NTkiLCJwIjoiaiJ9

**Descrição:**  
“Como Secretário Geral de Cultura, quero filtrar os eventos realizados pela Secretaria de Cultura dentro da IntegraTur.”  

**Conversa com o PO:**

"Nessa história o site deve fornecer ferramentas dentro da home para o usuário conseguir filtrar eventos diversos a partir dos filtros selecionados secretaria de turismo, secretaria da cultura ou ambas secretarias a partir de um botão no canto superior esquerdo da tela."

**Critérios de aceitação (CDA):**  
- A plataforma deve ter a opção “Secretaria de Cultura” como opção de filtro na página principal.  
- Ao clicar no filtro, devem aparecer as informações de todos os eventos que serão realizados pela Secretaria de Cultura.  
- A procura não pode ser trocada por outro filtro para que não ocorram conflitos.  

**Prioridade:** Média  
**Estimativa de Esforço:** 3 horas

---

### 9. Cadastro de Usuários  
**Link:** https://integratur.atlassian.net/browse/INT-2?atlOrigin=eyJpIjoiODMwNzRmYjRjOTNlNGQ1MThhZDUxM2FmOGYzNjExZDAiLCJwIjoiaiJ9

**Descrição:**  
“Como Coordenador de Projetos da Secretaria de Turismo, quero fazer o cadastro na plataforma IntegraTur, para que consiga utilizar de suas ferramentas.”  

**Conversa com o PO:**

"O usuário deverá ter ferramentas para cadastrar sua conta no primeiro contato com a plataforma, nesta tela deverá ter algumas boxs para o usuário inserir email, senha e confirmar senha, e a plataforma deve saber diferenciar quais e-mails são institucionais ou não, após o preenchimento das credenciais será enviado um código de confirmação para criação da conta e após colocar o código correto a senha deverá ser criada".

**Critérios de aceitação (CDA):**  
- A plataforma deve aceitar minhas informações pessoais como corretas.  
- Ao clicar no botão de cadastro, deve aparecer uma confirmação de que o usuário não é robô.  
- A plataforma deve permitir que somente usuários que trabalham em uma das Secretarias entrem.  
- A confirmação de cadastro deve ser acelerada, evitando travamentos e transtorno ao usuário.  

**Prioridade:** Alta  
**Estimativa de Esforço:** 5 horas  

---

### 10. Mapa de Eventos  
**Link:** https://integratur.atlassian.net/browse/INT-8?atlOrigin=eyJpIjoiOWIxNWNhM2RiMTRlNGYxZDhjYTU3NGY0NTNlN2M4NjYiLCJwIjoiaiJ9

**Descrição:**  
"Como secretário de Turismo, eu quero visualizar os eventos no mapa para monitorar a distribuição geográfica e identificar oportunidades de promoção turística."  

**Conversa com o PO:**

"Nesta funcionalidade, o usuário será capaz de visualizar os eventos distribuídos em forma geográfica em um mapa, e o mapa deverá ter um pin vermelho mostrando onde tem certo evento".

**Critérios de Aceitação:**  
- O mapa deve carregar automaticamente ao acessar a página.  
- Os eventos devem ser exibidos como marcadores geolocalizados.  
- Ao clicar em um marcador, um card deve exibir detalhes como nome do evento, data, local e organizador.  
- Deve haver um campo de busca por cidade ou CEP para filtrar eventos por localização.  
- O sistema deve permitir a navegação entre diferentes regiões para uma visão mais ampla dos eventos.  

**Prioridade:** Alta  
**Estimativa de esforço:** 5 horas  

## 🎨 Storyboard - Cadastro de Evento

**Link:** https://integratur.atlassian.net/browse/INT-13?atlOrigin=eyJpIjoiNjQxOTQxY2EwNzdjNGIwM2I5NDQ2ZWIyY2EzYTE2MjUiLCJwIjoiaiJ9

### **Tela 1: Formulário Base**
![Tela 1 - Estrutura Inicial](./assets/sb%20cadastrar%20novo%20evento/WhatsApp%20Image%202025-03-31%20at%2003.34.08.jpeg)  
**Fluxo:**  
- Preenchimento das **Informações Básicas** (Título, Responsável, Local, Descrição).  


---

### **Tela 2: Preenchimento Parcial**  
![Tela 2 - Dados Parciais](./assets/sb%20cadastrar%20novo%20evento/WhatsApp%20Image%202025-03-31%20at%2003.34.08%20(1).jpeg)  
**Destaques:**  
- Exemplo de evento: "Oficina do Bolo" (data 23/03/2025).  


---

### **Tela 3: Confirmação**  
![Tela 3 - Evento Salvo](./assets/sb%20cadastrar%20novo%20evento/WhatsApp%20Image%202025-03-31%20at%2003.34.09.jpeg)  
**Feedback do Sistema:**  
- Mensagem de sucesso: *"Evento Salvo Com Sucesso!"*.  

## 🔍 Storyboard - Pesquisa de Eventos na Home

**Link:** https://integratur.atlassian.net/browse/INT-14?atlOrigin=eyJpIjoiYWIwMjI2NDE2MmJjNDMzZDhkZWM3OTE0OWZiNGZiNTMiLCJwIjoiaiJ9

### **Tela 1: Home**
![Tela 1 - Filtros e Listagem](./assets/sb%20pesquisa%20na%20home/pesquisa%20na%20home%201.jpeg)  
**Fluxo:**  
**Filtros por categoria**: Checkboxes para "Secretaria de Cultura" e "Secretaria de Turismo" (ainda não selecionados).  

---

### **Tela 2: Barra de pesquisa **  
![Tela 2 - Evento Filtrado](./assets/sb%20pesquisa%20na%20home/pesquisa%20na%20home%202.jpeg)  
**Ação do Usuário:**  
- Usa barra de pesquisa **"Oficina de Maracatu"**.  
**Resultado:**  
- Exibe apenas **"Oficina de Maracatu"** (15/07/2025) com detalhes completos:  
  - Descrição do evento.  
  - Responsável: "Maria Dolores".  
  - Botão "Saiba Mais" ativo.  

---

### **Tela 3: Busca sem Resultados**  
![Tela 3 - Nenhum Resultado](./assets/sb%20pesquisa%20na%20home/pesquisa%20na%20home%203.jpeg)  
**Ação do Usuário:**  
- Busca por **"Festival Gastronômico"** (sem selecionar filtros).  
**Feedback do Sistema:**  
- Mensagem clara: *"Nenhum resultado encontrado para 'Festival Gastronômico'"*.  

## 📅 Storyboard - Calendário de Eventos

**Link:** https://integratur.atlassian.net/browse/INT-15?atlOrigin=eyJpIjoiYTM3MjU1YTZjODk1NGFmM2IyNTY3ZmQ0MzY0MzkxZjkiLCJwIjoiaiJ9

### **Tela 1: Visão Mensal**
![Tela 1 - Visão do Mês](./assets/sb%20calendario%20de%20eventos/Calendario%201.jpeg)    
**Menu de Filtros**:  
   - Opções por categoria (Todos, Localização, CEP).  
   - Filtro por tipo de evento e mês (Abril 2025 selecionado).  
**Grade do Calendário**:  
   - Visualização semanal com dias 1 a 26 de abril.  
   - Destaque para dias com eventos (ex.: 23/04 - Oficina do Bolo).  


---

### **Tela 2: Detalhes do Evento **  
![Tela 2 - Detalhes](./assets/sb%20calendario%20de%20eventos/Calendario%202.jpeg)  
**Ação do Usuário:**  
- Clica no evento "Oficina do Bolo" (23/04/2025).  
**Informações Exibidas:**  
- **Dados Básicos**:  
  - Data/hora: 23 de Abril, 09:00-12:00.  
  - Local: Centro de Convenções (endereço completo). 

## 🔐 Storyboard - Fluxo de Login e Cadastro

**Link:** https://integratur.atlassian.net/browse/INT-11?atlOrigin=eyJpIjoiYWVmMmVhYjU3NzUzNDVlOThkZTRlYzg3YjQ2NWNmOTEiLCJwIjoiaiJ9

### **Tela 1: Página de Login**
![Tela 1 - Login](./assets/sb%20login_cadastro/login%201.png)  
**Elementos Chave:**  
- Campos para **e-mail institucional** e **senha**.  
- Opções:  
  - "Salvar login" (lembrar usuário).  
  - "Esqueci a senha".  
- Botões principais:  
  - **"Entrar"** (submissão).  
  - **"Registre-se"** (redireciona para cadastro).  

---

### **Tela 2: Login Bem-Sucedido**  
![Tela 2 - Sucesso](./assets/sb%20login_cadastro/login%202.png)  
**Feedback do Sistema:**  
- Mensagem: *"Login efetuado com sucesso!"*.  
- Exibe **nome do usuário** e **e-mail institucional**.  
- Botão **"Continuar"** para acesso à dashboard.  

---

### **Tela 3: Login Falhou**  
![Tela 3 - Erro](./assets/sb%20login_cadastro/login%203.png)  
**Tratamento de Erro:**  
- Mensagem clara: *"Falha no Login: Usuário ou senha incorretos"*.  
- Opções:  
  - **"Tentar novamente"** (volta à Tela 1).  
  - **"Criar uma conta"** (redireciona para Tela 4).  

---

### **Tela 4: Cadastro de Usuário**  
![Tela 4 - Cadastro](./assets/sb%20login_cadastro/login%204.png)  
**Formulário de Registro:**  
- Campos obrigatórios:  
  - Nome completo, CPF, e-mail, senha (com validação em tempo real).  
  - Data de nascimento e gênero (opcional).  
- Botões:  
  - **"Entrar"** (submissão).  
  - **"Fazer login"** (para usuários já cadastrados).  

## 🗺️ Storyboard - Fluxo do Mapa de Eventos

**Link:** https://integratur.atlassian.net/browse/INT-12?atlOrigin=eyJpIjoiMTZlOWY0MzY5ZDlmNDQyOGI3NzY0MTQxN2NkYzFkYmMiLCJwIjoiaiJ9

### **1. Home** *(Home → Mapa)*  
![Home do Sistema](./assets/sb%20mapa/mapa%201.png) *(Imagem existente reutilizada)*  
**Ação do Usuário:**  
- Clica em **"Mapa de eventos"** no menu lateral.  
**Sistema:**  
- Redireciona para a tela de mapa de eventos.  

---

### **2. Visualização do Mapa** *(Mapa base com eventos)*  
![Mapa com Pins](./assets/sb%20mapa/mapa%202.png) *(Imagem adaptada como exemplo)*  
**Funcionalidades:**  
- Pin vermelho indicando evento.  
- Barra de busca superior com placeholder: *"Buscar por CEP ou endereço..."*.  

---

### **3. Detalhes do Evento** *(Ao clicar no pin)*  
![Detalhes do Evento](./assets/sb%20mapa/mapa%203.png) *(Imagem reutilizada)*  
**Dados exibidos:**  
- Nome, data, localização física.  
- Botões: *"Editar"* (para gestores) e *"Compartilhar"*.  

---

### **4. Busca por CEP** *(Filtro geográfico)*  
![Busca por CEP](./assets/sb%20mapa/mapa%204.png) *(Imagem adaptada)*  
**Fluxo:**  
- Usuário digita CEP (ex.: `50000-000`).  
- Mapa ajusta a visualização para a região.  
- Exibe apenas eventos no raio de 5km.  

## 📋 Backlog do Produto - Sprint 27-30 Março

### 🎯 Objetivo da Sprint
Produzir histórias, storyboards e sketches para atender os 15 entregáveis do "Entrego-1"

---

### 📝 Itens do Backlog

| Tipo        | Item                                | Status     |
|-------------|-------------------------------------|------------|
| História    | Cadastrar Evento                    | ✅         |
| História    | Procurar Evento na Home             | ✅         |
| História    | Login                               | ✅         |
| História    | Filtrar Evento da Secretaria Cultura| ✅         |
| História    | Chat de Secretarias                 | ✅         |
| História    | Cadastro de Usuários                | ✅         |
| História    | Calendário de Eventos               | ✅         |
| História    | Orçamento do Evento                 | ✅         |
| História    | Mapa de Eventos                     | ✅         |
| História    | Cadastrar Fornecedor                | ✅         |
| Storyboard  | Cadastro e Login                    | ✅         |
| Storyboard  | Cadastrar Evento                    | ✅         |
| Storyboard  | Procurar Evento na Home             | ✅         |
| Storyboard  | Calendário de Eventos               | ✅         |
| Storyboard  | Mapa de Eventos                     | ✅         |

![Backlog jira](./assets/BACKLOG%20sprint%201%20.png)

## Cadastrar Eventos
![Diagrama UML de atividades- Cadastro de eventos](./assets/UMLA_CADASTRAR%20EVENTOS.jpeg)
**Screencast Cadastro de eventos:** https://youtu.be/CtRIo2G_OgA






--- 