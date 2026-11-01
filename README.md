# Monitoramento de Painéis
Essa API recebe a requisição da automação com PyAutoGui e exibe no Dashboard o status de todos os painéis da empresa.
Exemplo: Clínicos, Baxter (Monitoramento de Camas Hospitalares), Painel de Chamada, Totens, Grafana, etc.

## O que ela resolve
Antes: Quando tinha algum problema com o painel ou quando o computador reiniciava por motivos diversos a TI só ficava ciente do problema através de chamado ou ronda Técnica.
Depois: A automação em questão, gera uma requisição para outra aplicação API que tem um Dashboard com todos os paineis exibidos na sala da TI centralizado, avisando que tal painel esta offline.

## Funcionalidades
- Exibe os status dos painéis Online/Offline

## Tecnologias
- Python 3.9.12
- Django 4.2
- Django Rest Framework
- SQLite 3

## Como rodar

### 1. Clone o repositório
```bash
git clone https://github.com/futuroinfor/api_painel_baxter.git
cd api_painel_baxter
```
### 2. Crie e ative um ambiente virtual
Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
### 4. Execute
```bash
python run_server.py
```
## Autor
Romilson J Tenorio
- LinkedIn: [Romilson J Tenório](https://www.linkedin.com/in/romilsontenorio/)
- E-mail: romilson.tenorio@hotmail.com
## Licença
Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.
