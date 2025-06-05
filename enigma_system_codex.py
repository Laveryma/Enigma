
from openai import ChatCompletion
import re

def call_gpt(prompt, system_msg="You are a helpful assistant.", model="gpt-4-turbo"):
    response = ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def enigma_forecast(question):
    system_prompt = "You are ENIGMA, a geopolitical forecasting model."
    return call_gpt(question, system_msg=system_prompt)

def ciren_review(forecast):
    system_prompt = (
        "You are CIREN, a critique engine that evaluates the structural integrity of forecasts. "
        "Score the input from 1 to 10, explain the weaknesses, and provide the score at the end like: SCORE: 6"
    )
    return call_gpt(forecast, system_msg=system_prompt)

def hephaestus_refine(ciren_output):
    system_prompt = (
        "You are HEPHAESTUS, a repair module that upgrades a forecast based on CIREN's critique. "
        "Improve the structure and reasoning of the forecast accordingly."
    )
    return call_gpt(ciren_output, system_msg=system_prompt)

def extract_score(text):
    match = re.search(r"SCORE:\s*(\d+)", text)
    return int(match.group(1)) if match else 0

def run_enigma_loop(question):
    print(f"\U0001F9E0 Forecast Question: {question}")
    forecast = enigma_forecast(question)
    print("\n\U0001F4E5 Initial Forecast:\n", forecast)

    for iteration in range(10):
        ciren_output = ciren_review(forecast)
        score = extract_score(ciren_output)
        print(f"\n\U0001F50E CIREN Review [Score {score}/10]:\n{ciren_output}")

        if score >= 10:
            print("\n✅ Final Forecast Approved")
            return forecast

        forecast = hephaestus_refine(ciren_output)
        print(f"\n\U0001F527 HEPHAESTUS Refinement:\n{forecast}")

    print("\n⚠️ Max iterations reached. Final score:", score)
    return forecast

# Example run
run_enigma_loop("Will China attempt a blockade of Taiwan before 2028?")
