from openai import OpenAI
client = OpenAI()

f = open("./text.txt")
article_html = f.read()
print(article_html)
prompt = f"Is it a good news or bad news for the ticker AUTL? Please answer with yes or no and give 3 reasons from the article. {article_html}"
# prompt = "Can you give the Python code to get article title and body part from the HTML response?"

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user", 
            "content": prompt
        },
    ],
    # response_format={
    #     "type": "json_schema",
    #     "json_schema": {
    #         "name": "email_schema",
    #         "schema": {
    #             "type": "object",
    #             "properties": {
    #                 "email": {
    #                     "description": "The email address that appears in the input",
    #                     "type": "string"
    #                 },
    #                 "additionalProperties": False
    #             }
    #         }
    #     }
    # }
)

print(response.choices[0].message.content);
