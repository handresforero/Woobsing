#conda create -n Spinner python=3.9
#conda activate Spinner1
#cd D:\Woobsing\Spinner

#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################

# # from nltk.tokenize import word_tokenize
# # from nltk.tag import pos_tag
# # from nltk.corpus import wordnet as wn

# # def tag(sentence):
# #  words = word_tokenize(sentence)
# #  words = pos_tag(words)
# #  return words

# # def paraphraseable(tag):
# #  return tag.startswith('NN') or tag == 'VB' or tag.startswith('JJ')

# # def pos(tag):
# #  if tag.startswith('NN'):
# #   return wn.NOUN
# #  elif tag.startswith('V'):
# #   return wn.VERB

# # def synonyms(word, tag):
# #     lemma_lists = [ss.lemmas() for ss in wn.synsets(word, pos(tag))]
# #     lemmas = [lemma.name() for lemma in sum(lemma_lists, [])]
# #     return set(lemmas)

# # def synonymIfExists(sentence):
# #  for (word, t) in tag(sentence):
# #    if paraphraseable(t):
# #     syns = synonyms(word, t)
# #     if syns:
# #      if len(syns) > 1:
# #       yield [word, list(syns)]
# #       continue
# #    yield [word, []]

# # def paraphrase(sentence):
# #  return [x for x in synonymIfExists(sentence)]

# # paraphrase("The quick brown fox jumps over the lazy dog")










# import nltk
# import random
# import numpy as np
# from bs4 import BeautifulSoup

# positive_reviews = BeautifulSoup(open('electronics/positive.review').read())
# positive_reviews = positive_reviews.findAll('review_text')

# trigrams = {}
# for review in positive_reviews:
#     s = review.text.lower()
#     tokens = nltk.tokenize.word_tokenize(s)
#     for i in xrange(len(tokens) - 2):
#         k = (tokens[i], tokens[i+2])
#         if k not in trigrams:
#             trigrams[k] = []
#         trigrams[k].append(tokens[i+1])
        
# trigrams_probabilities = {}
# for k, words in trigrams.iteritmes():
#     if len(set(words)) > 1:
#         d = {}
#         n = 0
#         for w in words:
#             if w not in d:
#                 d[w] = 0
#             d[w] += 1
#         for w,c in d.iteritems():
#             d[w] = float(c) / n
#         trigrams_probabilities[k] = d
        
# def random_sample(d):
#     r = random.random()
#     cumulative = 0
#     for w, p in d.iteritems():
#         cumulative += p
#         if r < cumulative:
#             return w

# def test_spinner():
#     review = random.choice(positive_reviews)
#     s = review.text.lower()
#     print("Original: ",s)
#     tokens = nltk.tokenize.word_tokenize(s)
#     for i in xrange(len(tokens) - 2):
#         if random.random() < 0.2:
#             k = (tokens[i], tokens[i+2])
#             if k in trigrams_probabilities:
#                 w = random_sample(trigrams_probabilities[k])
#                 tokens[i+1] = w
#     print("Spun: ")
#     print("".join(tokens).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!"))




import os
os.chdir("gpt-2")



import json
import os
import numpy as np
import tensorflow as tf
import model, sample, encoder



def interact_model(
    model_name,
    seed,
    nsamples,
    batch_size,
    length,
    temperature,
    top_k,
    models_dir
):
    models_dir = os.path.expanduser(os.path.expandvars(models_dir))
    if batch_size is None:
        batch_size = 1
    assert nsamples % batch_size == 0

    enc = encoder.get_encoder(model_name, models_dir)
    hparams = model.default_hparams()
    with open(os.path.join(models_dir, model_name, 'hparams.json')) as f:
        hparams.override_from_dict(json.load(f))

    if length is None:
        length = hparams.n_ctx // 2
    elif length > hparams.n_ctx:
        raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

    with tf.Session(graph=tf.Graph()) as sess:
        context = tf.placeholder(tf.int32, [batch_size, None])
        np.random.seed(seed)
        tf.set_random_seed(seed)
        output = sample.sample_sequence(
            hparams=hparams, length=length,
            context=context,
            batch_size=batch_size,
            temperature=temperature, top_k=top_k
        )

        saver = tf.train.Saver()
        ckpt = tf.train.latest_checkpoint(os.path.join(models_dir, model_name))
        saver.restore(sess, ckpt)

        while True:
            raw_text = input("Model prompt >>> ")
            while not raw_text:
                print('Prompt should not be empty!')
                raw_text = input("Model prompt >>> ")
            context_tokens = enc.encode(raw_text)
            generated = 0
            for _ in range(nsamples // batch_size):
                out = sess.run(output, feed_dict={
                    context: [context_tokens for _ in range(batch_size)]
                })[:, len(context_tokens):]
                for i in range(batch_size):
                    generated += 1
                    text = enc.decode(out[i])
                    print("=" * 40 + " SAMPLE " + str(generated) + " " + "=" * 40)
                    print(text)
            print("=" * 80)