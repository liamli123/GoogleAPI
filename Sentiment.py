from google.cloud import language

def sentiment(text):
    client=language.Client()
    document=client.document_from_text(text)
    sent_analysis=document.analyze_sentiment()
    for item in dir(client):
         print (item)
    senti = sent_analysis.sentiment
    return senti

if __name__ == '__main__':
    senti=sentiment('http://www.marketwatch.com/story/amazon-adding-1000-full-time-jobs-with-michigan-fulfillment-center-2017-09-14?siteid=yhoof2&yptr=yahoo')
