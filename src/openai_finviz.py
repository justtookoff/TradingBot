import glob
from openai import OpenAI

client = OpenAI()
article_time = "250101_143106"

ticker_good_count = dict()
ticker_bad_count = dict()

for file_path in glob.glob("./../articles/" + article_time + "/*.txt"):
    # print(file_path)
    article_title = file_path.split("/")[-1][:-4]
    article_ticker = article_title.split("_")[0]
    print(article_title, article_ticker, end=' ')

    with open(file_path, "r") as f:
        article_content = f.read()

    # prompt = f"Is it a good news or bad news for the ticker {article_ticker}}? Please answer with yes or no and give 3 reasons from the article. {article_content}"
    prompt = f"Is it a good news or bad news for the ticker {article_ticker}? Please answer with the format of good or bad. {article_content}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user", 
                "content": prompt
            },
        ],
    )

    print(response.choices[0].message.content)

    if "Good" in response.choices[0].message.content:
        if article_ticker in ticker_good_count:
            ticker_good_count[article_ticker] += 1
        else:
            ticker_good_count[article_ticker] = 1
    elif "Bad" in response.choices[0].message.content:
        if article_ticker in ticker_bad_count:
            ticker_bad_count[article_ticker] += 1
        else:
            ticker_bad_count[article_ticker] = 1

sorted_ticker_good_count = dict(sorted(ticker_good_count.items(), key=lambda item: item[1], reverse=True))
sorted_ticker_bad_count = dict(sorted(ticker_bad_count.items(), key=lambda item: item[1], reverse=True))

print(sorted_ticker_good_count)
print(sorted_ticker_bad_count)
    
