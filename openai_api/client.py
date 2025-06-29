import openai
import os

# Corrigido: carrega a chave da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_car_ai_bio(model, brand, year):
    prompt = f'''
    Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. 
    Descreva especificações técnicas desse modelo de carro.
    '''

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista em carros."},
                {"role": "user", "content": prompt.strip()},
            ],
            temperature=0.7,
            max_tokens=250,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"[OpenAI ERROR] {e}")
        return "Descrição automática indisponível no momento."
