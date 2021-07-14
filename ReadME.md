## **Table of Contents**
- [E13 - Klog de Posts](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4a_e_01_sql-alchemy-n-jinja.html&ref=master#mcetoc_1egvo5vbn3)
  - [Objetivos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4a_e_01_sql-alchemy-n-jinja.html&ref=master#mcetoc_1f7i3b0bd0)
  - [Rotas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4a_e_01_sql-alchemy-n-jinja.html&ref=master#mcetoc_1eiob4uhce)
    - [GET /api](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4a_e_01_sql-alchemy-n-jinja.html&ref=master#mcetoc_1eok97uap0)
    - [GET /api/posts](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4a_e_01_sql-alchemy-n-jinja.html&ref=master#mcetoc_1f7i68g0o2)
    - [GET /api/posts/](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4a_e_01_sql-alchemy-n-jinja.html&ref=master#mcetoc_1f7i68g0o3)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4a_e_01_sql-alchemy-n-jinja.html&ref=master#mcetoc_1f362b6b12)
  - [Repositório](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4a_e_01_sql-alchemy-n-jinja.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4a_e_01_sql-alchemy-n-jinja.html&ref=master#mcetoc_1eh146n6m3)
# **E13 - Klog de Posts**
Para esta entrega, você criará um sistema de postagem de cards simulando um blog.

## **Objetivos**
Praticar os conhecimentos em templates e Jinja, criação e conexão com banco de dados utilizando models e Flask-SQLAlchemy. Você terá uma autonomia maior nessa entrega para estilizar seu layout de acordo com o que achar melhor, utilizando as mecanicas do Bootstrap + Jinja2. Também ficará a seu cargo a organização dos diretórios, arquivos e métodos do seu sistema, seguindo os padrões vistos até agora de Flask Factory, Blueprints, macros, filters e includes se assim desejar. A unica restrição que teremos será a nomenclatura url das rotas seguindo as orientações de api RESTFUL. Ao final, o seu sistema deverá ser **capaz de registrar dados de postagens de um blog e listar dados das postagens.** Crie sua model com os campos que julgar necessários para um post.

## **Rotas**
### **GET /api**
Esta rota ficará responsável por listar todas as postagens armazenadas no banco.

- **Procedimentos**:
  - Caso não exista postagens cadastradas, mostrar alguma mensagem que notifique o usuario de que não há posts.
  - Caso exista postagens, renderizar uma página HTML mostrando todos os posts em formato de grid ou como achar melhor.
  - **Extra**:
    - Monte um sistema de paginação em que cada página pode ter 5 posts.
    - Utilize um mecanismo no HTML para transitar entre as rotas pela página.


|**Exemplo de layout para GET /posts**|
| :- |
|<p>![](Aspose.Words.4a141e8b-0132-4d73-a883-11ac676cbe87.001.png)</p><p></p><p></p>|

### **GET /api/posts**
Esta rota ficará responsável por recolher as informações de um form e fazer a conexão com algo que salve os dados no banco. Para isso será necessário criar uma rota auxiliar que ficará responsável por pegar o post gerado pelo submit do HTML renderizado por GET /api/posts.

- **Procedimentos**:
  - Renderizar um formulário para capturar as informações que voce achar mais relevantes para criação de um post no blog.
  - Assim que um post for criado, redirecionar para a rota **/api** para verificar se o post está listado de fato.

|**Exemplo de formulário**|
| :- |
|![](Aspose.Words.4a141e8b-0132-4d73-a883-11ac676cbe87.002.png)|

### **GET /api/posts/<post\_id>**
Esta rota ficará responsável por lista unitariamente um post.

- **Procedimentos**:
  - Renderizar um HTML que mostre somente o post indicado na url.
  - Se o post não existir, exibir uma mensagem personalizada de **404 - Not Found**.

|**/api/posts/1**|
| :- |
|![](Aspose.Words.4a141e8b-0132-4d73-a883-11ac676cbe87.003.png)|


|**404 - Not Found**|
| :- |
|![](Aspose.Words.4a141e8b-0132-4d73-a883-11ac676cbe87.001.png)|

-----
# **Entregáveis**
## **Repositório**
- Link do **repositório** do **GitLab**
- **Código fonte:**
  - Estrutura de diretórios de uma **aplicação Flask**
  - **.env.example**
  - **requirements.txt**
- **Privacidade**
  - Incluir **ka-br-out-2020-correcoes** como reporter.
-----
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|2|Rota GET /api|Acessada a rota|Renderize uma template HTML listando todos os posts do banco de dados|
|2|Rota GET /api/posts|Acessada a rota|Renderize um formulário com os campos necessários para a adição do post no banco de dados.|
|2|Rota auxiliar POST /api/posts|Enviado os dados do form renderizado pelo GET /api/posts|Recolhe os dados do formulário para a utilização dentro do sistema.|
|2|Conexão com o banco de dados|Verificada a integridade do transporte dos dados|Que as rotas consumam e enviem dados para o banco corretamente|
|1|Estilização básica|Acessada as templates através das rotas|Que seja utilizado alguma forma de estilização básica para a rendeziração ficar apresentável|
|1|Arquivos no gitlab|Verificado os envios|Que contenha os arquivos .env.example e requirements.txt devidamente preechidos|

**Boa diversão, devs! 🧛‍♀️**

