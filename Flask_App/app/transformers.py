from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline, AutoModelForSeq2SeqLM
import pickle

def save_transformer_models_as_pickle():
    # save model as a pickle file
    model_name = "t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

    pickle.dump(summarizer, open('./model/model_summarizer.pickle', mode='wb'))    


def get_summarizer(input_text):
    # get pickle file to summarize text
    
    model_summarizer =  pickle.load(open('./model/model_summarizer.pickle',mode='rb'))
    summary_text = model_summarizer(input_text, max_length=100, min_length=10)[0]["summary_text"]

    return summary_text