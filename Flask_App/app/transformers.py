from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline, AutoModelForSeq2SeqLM
import pickle
import redis

def save_summarizer_model_as_pickle():
    # save model as a pickle file
    model_name = "t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

    #pickle.dump(summarizer, open('./model/model_summarizer.pickle', mode='wb'))    

    return pickle.dumps(summarizer)

def load_summarizer_pickle_to_redis():
    model_summarizer = save_summarizer_model_as_pickle()
    r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
    r.set('summarizer', model_summarizer, ex=31536000)

def get_summarizer(input_text):
    
    # get pickle file from redis to summarize text

    r = redis.Redis(host='localhost', port=6379, db=0)
    model_summarizer = pickle.loads(r.get('summarizer'))
    summary_text = model_summarizer(input_text, max_length=100, min_length=10)[0]["summary_text"]
    
    return summary_text
