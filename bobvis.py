# from dotenv import load_dotenv
# import openai 
# import os 

# load_dotenv()


# KEY =os.getenv('KEY_API')


# def bobvis_reponse(prompt):
#     reponse = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=50,
#         presence_penalty=0,
#         frequency_penalty=0,
#         best_of=1,
#     )

#     reponse_dict = reponse.get("choices")
#     if reponse_dict and len(reponse_dict) > 0:
#         prompt_reponse = reponse_dict[0]["text"]
#     return  prompt_reponse,