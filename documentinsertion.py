from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['study']  
collection = db['test']  
document = {
    "_id":5,
    "question": ''' Discuss various methods of importing modules in Python programs.
Which method is best?. Explain.''',
    "answer": "AI stands for Artificial Intelligence...",
    "est_time":30 ,
    "paper":"mod"#"pre"

}


collection.insert_one(document)

print("Document inserted successfully.")
