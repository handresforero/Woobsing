#conda activate Vitale
#cd D:\Woobsing\Vitale
#conda install -c conda-forge spacy
#python -m spacy download es

# import spacy

# nlp = spacy.load('es_core_news_sm')
# text = "Soy un texto. Normalmente soy más largo y más grande. Que no te engañe mi tamaño."
# doc = nlp(text) # Crea un objeto de spacy tipo nlp
# #tokens = [t.orth_ for t in doc] # Crea una lista con las palabras del texto
# #print(tokens)

# doc = nlp(text)
# lexical_tokens = [t.orth_ for t in doc if not t.is_punct | t.is_stop] # Esta linea i la anterior normalizan el texto
# print(lexical_tokens)

# def normalize(text):
#     doc = nlp(text)
#     words = [t.orth_ for t in doc if not t.is_punct | t.is_stop]
#     lexical_tokens = [t.lower() for t in words if len(t) > 3 and     
#     t.isalpha()]
#     return lexical_tokens
#     lemmas = [tok.lemma_.lower() for tok in lexical_tokens]
# word_list = normalize("Soy un texto que pide a gritos que lo procesen. Por eso yo canto, tú cantas, ella canta, nosotros cantamos, cantáis, cantan…")

# print(word_list)

# text = "Soy un texto que pide a gritos que lo procesen. Por eso yo canto, tú cantas, ella canta, nosotros cantamos, cantáis, cantan…"
# doc = nlp(text)
# lemmas = [tok.lemma_.lower() for tok in doc]
# lemmas_no_pron = [tok.lemma_.lower() for tok in doc if tok.pos_ != 'PRON']
# print(lemmas_no_pron)



# #pip install spacy-stanza
# from spacy_stanza import StanzaLanguage
# from spacy_stanza import 

# text = "personas, ideas, cosas"

# snlp = stanza.Pipeline(lang="es")
# nlp = StanzaLanguage(snlp)
# doc = nlp(text)
# for token in doc:
#     print(token.lemma_)


# #pip install nlp
# #pip install spark-nlp
# #conda install -c johnsnowlabs spark-nlp
# import sparknlp
# from sparknlp.common import *
# import com.johnsnowlabs.nlp
# from sparknlp.base import DocumentAssembler, Finisher, EmbeddingsFinisher, TokenAssembler
# from sparknlp.pretrained import ResourceDownloader
# from sparknlp import LemmatizerModel

# lemmatizer = LemmatizerModel.pretrained("lemma", "es") \
#         .setInputCols(["token"]) \
#         .setOutputCol("lemma")
# nlp_pipeline = Pipeline(stages=[document_assembler, tokenizer, lemmatizer])
# light_pipeline = LightPipeline(nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text")))
# results = light_pipeline.fullAnnotate("Además de ser el rey del norte, John Snow es un médico inglés y líder en el desarrollo de la anestesia y la higiene médica.")

# print(results)

import nltk
#nltk.download()
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))