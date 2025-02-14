# **auto-mr-docs** 🚀  
Automação Inteligente para Descrições de Merge Requests no GitLab

## **Índice**
1. [Visão Geral](#-visão-geral)  
2. [Recursos](#-recursos)  
3. [Como Funciona](#-como-funciona)  
4. [Como Utilizar](#-como-utilizar)  
5. [Status de Desenvolvimento](#-status-de-desenvolvimento)  
6. [Licença](#-licença)  
7. [Contribuindo](#-contribuindo)  
8. [Contato](#-contato)  

---

## **🚀 Visão Geral**  
O **auto-mr-docs** é um bot que gera descrições detalhadas para Merge Requests (MRs) no **GitLab** de forma automática. Ele analisa os commits associados ao MR e utiliza **modelos de IA** (podendo ser **Ollama** ou **OpenAI**) para criar descrições claras, bem estruturadas e profissionais. O objetivo é reduzir o tempo de escrita manual e manter uma **documentação padronizada** e **informativa**.

---

## **✨ Recursos**  
- **Geração Automática de Descrições** para MRs no GitLab  
- **Integração Simples via GitLab CI/CD** (sem necessidade de serviços externos)  
- **Suporte a Diferentes Modelos de IA**  
  - **Ollama** (execução local, sem precisar de serviços externos)  
  - **OpenAI** (para quem prefere usar modelos na nuvem)  
- **Execução via Docker** – Facilita a implementação e a configuração  
- **Redução de Tempo e Erros Humanos** – Descrições mais padronizadas e informativas  

---

## **⚙️ Como Funciona?**  
1. O bot analisa os commits do Merge Request.  
2. Envia os dados para o modelo de IA configurado (Ollama ou OpenAI).  
3. Gera uma descrição detalhada e estruturada automaticamente.  
4. Atualiza a descrição do MR no GitLab, garantindo maior consistência entre as alterações propostas.  

---

## **🛠️ Como Utilizar?**  

Para utilizar o **auto-mr-docs** em seu fluxo de trabalho no GitLab, siga estes passos:  
1. **Escolha** o modelo de IA que deseja utilizar (Ollama ou OpenAI).  
2. **Configure** as variáveis de ambiente necessárias (por exemplo, `OPENAI_API_KEY` para usar o OpenAI).  
3. **Adicione** um estágio ao seu **`.gitlab-ci.yml`** que chame o `auto-mr-docs` quando um Merge Request for criado ou atualizado.

### **Exemplo de configuração do GitLab CI/CD**  
Abaixo está um **exemplo básico** de como integrar o **auto-mr-docs** usando a imagem oficial com a tag **latest**:

```yaml
image: automrdocs/auto_mr_docs:latest

stages:
  - merge_request_analysis

merge_request_summarization:
  stage: merge_request_analysis
  script:
    - |
      auto-mr-docs summarize \
        --mode openai \
        --api-key "$OPENAI_API_KEY" \
        --gitlab-token "$GITLAB_TOKEN" \
        --project-id "$CI_PROJECT_ID" \
        --mr-id "$CI_MERGE_REQUEST_IID"

  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_IID'
      when: on_success
```

> **Notas Importantes**  
> - As variáveis `CI_PROJECT_ID` e `CI_MERGE_REQUEST_IID` já são definidas automaticamente pelo GitLab quando o pipeline é executado em um Merge Request.  
> - Caso utilize **Ollama**, é necessário ter o executável **ollama** instalado e disponível no ambiente (seja localmente ou no container) para que o `auto-mr-docs` consiga chamá-lo.  
> - Se estiver usando **OpenAI**, lembre-se de definir e exportar a variável de ambiente `OPENAI_API_KEY`.  
> - Ajuste as regras de execução (`rules`) conforme o seu fluxo de trabalho.  

---

## **📦 Status de Desenvolvimento**  
- O projeto encontra-se em fase de implementação.  
- Futuramente, serão adicionadas instruções mais completas sobre configuração e uso em diferentes cenários.  

---

## **📝 Licença**  
Este projeto está licenciado sob a **GNU General Public License v3.0 (GPL-3.0)**.  
Isso significa que você pode usar, modificar e distribuir o código, desde que as modificações sejam distribuídas sob a mesma licença.

Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).

---

## **🤝 Contribuindo**  
Contribuições são sempre bem-vindas!  
- **Issues**: Abra uma para sugerir melhorias, relatar bugs ou discutir ideias.  
- **Pull Requests**: Fique à vontade para enviar melhorias de código ou documentação.  

---

## **📩 Contato**  
Em caso de dúvidas, sugestões ou feedback, entre em contato pelos canais disponíveis no repositório ou abra uma **issue**.