import subprocess
from logger import LoggerConfig

logger = LoggerConfig.get_logger()

class LocalModel:
    # MODEL_NAME = "phi"
    MODEL_NAME = "mistral"
    
    @staticmethod
    def generate_description_by_commits(commits: list[str]) -> str:
        if not commits:
            logger.warning("Nenhum commit foi passado para geração da descrição.")
            return "Nenhuma descrição disponível."
        
        prompt = f"""
You are an AI assistant specialized in generating structured and professional Merge Request summaries.

## **Task**
Your job is to take the commit messages below and transform them into a **polished, professional, and structured Merge Request summary** in **Markdown format**.

## **Output Format**
Your response must follow **this exact Markdown structure**:

```
# Merge Request Summary

## New Features
(Only commits that introduce entirely new functionalities.)

## Bug Fixes
(Only commits that explicitly fix errors, incorrect behavior, or bugs.)

## Improvements & Refactoring
(Only commits that optimize, refactor, improve security, performance, or maintainability.)
```

---

## **🚨 STRICT RULES 🚨**
1️⃣ **Correctly categorize each commit:**
   - **If the commit adds a new feature,** it **MUST** go under `## New Features`.
   - **If the commit fixes a bug,** it **MUST** go under `## Bug Fixes`.
   - **If the commit improves, refactors, optimizes, or enhances security,** it **MUST** go under `## Improvements & Refactoring`.

2️⃣ **🚨 IMPORTANT RULE ABOUT LOGS 🚨**
   - Any commit related to **logging, monitoring, or tracking** **MUST** go under **"Improvements & Refactoring"**, **NOT "New Features"**.
   - **Examples:**
     ✅ `"Add logs for tracking failed login attempts"` → `## Improvements & Refactoring`  
     ❌ **WRONG:** `"Add logs for tracking failed login attempts"` in `## New Features`.  

3️⃣ **Keyword-based classification (STRICT).**
   - If the commit contains **“Add”**, **“Introduce”**, **“Implement”** → **New Features**  
   - If the commit contains **“Fix”**, **“Resolved”**, **“Correct”**, **“Patch”** → **Bug Fixes**  
   - If the commit contains **“Improve”**, **“Enhance”**, **“Optimize”**, **“Refactor”**, **“Update”**, **“Secure”**, **“Log”**, **“Track”** → **Improvements & Refactoring**  

4️⃣ **Do NOT alter the meaning of the commit messages.**
   - You may rewrite them in a more professional way, but the core meaning **MUST remain exactly the same**.

5️⃣ **DO NOT assume information.**
   - If a commit does not explicitly state that it is fixing a bug, **do NOT** place it under `## Bug Fixes`.
   - If a commit does not clearly add a new feature, **do NOT** place it under `## New Features`.

6️⃣ **No extra text, no assumptions, no reordering.**
   - DO NOT add an introduction or explanation before the list.
   - DO NOT summarize the changes; just rewrite them professionally while keeping their meaning.
   - DO NOT add bullet points outside the categories.

7️⃣ **Return only the structured Markdown response, formatted strictly as follows:**
```
# Merge Request Summary

## New Features
(If applicable, list the commits here.)

## Bug Fixes
(If applicable, list the commits here.)

## Improvements & Refactoring
(If applicable, list the commits here.)
```

---

### **Commit Messages**
{chr(10).join(commits)}
"""

        
        try:
            result = subprocess.run(
                ["ollama", "run", LocalModel.MODEL_NAME, prompt],
                capture_output=True, text=True, timeout=480
            )
            response = result.stdout.strip()
            
            if not response:
                logger.warning("O modelo retornou uma resposta vazia.")
                return "Erro ao gerar descrição automática."

            return response
        except Exception as e:
            logger.error(f"Erro ao executar o modelo local: {e}")
            return "Erro ao gerar descrição automática."
