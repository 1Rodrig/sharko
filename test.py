<<<<<<< HEAD
import openai

# ✅ CONFIGURATION
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Remplace par ta clé API
MODEL = "gpt-3.5-turbo"  # ou "gpt-4"

# Configuration de l’API
openai.api_key = API_KEY

# Fonction principale de chatbot
def run_chatbot():
    print("🤖 Bienvenue dans le Chatbot intelligent (tape 'exit' pour quitter)\n")
    conversation = []

    while True:
        user_input = input("Vous: ")

        if user_input.lower() in ['exit', 'quit']:
            print("👋 Fin de la session. À bientôt !")
            break

        conversation.append({"role": "user", "content": user_input})

        try:
            # Appel avec la nouvelle méthode API (nouvelle structure)
            response = openai.chat_completions.create(
                model=MODEL,
                messages=conversation
            )
            reply = response["choices"][0]["message"]["content"].strip()
            conversation.append({"role": "assistant", "content": reply})
            print("Bot:", reply)

        except Exception as e:
            print(f"[Erreur API] : {e}")
        except Exception as e:
            print(f"[Erreur interne] : {e}")

# Point d’entrée
if __name__ == "__main__":
    run_chatbot()