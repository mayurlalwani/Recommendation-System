import spacy

nlp = spacy.load('en_core_web_sm')


def enrich_text(_text):
    inherent_concepts = []
    enriched_concepts = []

    NER_TAGS = ['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART', 'LAW', 'LANGUAGE']

    doc = nlp(_text)  # This is a heavy op!
    for np in list(doc.noun_chunks):

        # Only keep adjectives and nouns, e.g. "good ideas"
        while len(np) > 1 and np[0].dep_ not in ('amod', 'compound'):
            np = np[1:]
        if len(np) > 1:
            # Merge the tokens, e.g. good_ideas
            np.merge(tag=np.root.tag_, lemma=np.text, ent_type=np.root.ent_type_)
    # Iterate over named entities
    for ent in doc.ents:
        if len(ent) > 1:
            # Merge them into single tokens
            ent.merge(tag=ent.root.tag_, lemma=ent.text, ent_type=ent.label_)
    token_strings = []
    for token in doc:
        tag = token.ent_type_ or token.pos_
        if (token.is_stop) or tag == 'PUNCT':  # or (token.pos_ != 'VERB' and token.pos_ != 'NOUN'):
            continue

        text = token.text.lower().replace(' ', '_')
        if ('_' in text) or tag in NER_TAGS:
            # inherent_concepts.append(text)
            token_strings.append('%s|%s' % (text, tag))
    # print(token_strings[0:-1])
    # print token_strings[0:-1]
    inherent_concepts = token_strings[0:-1]
    # enriched_concepts = self.get_similar_senses(inherent_concepts)
    inherent_concepts = ' '.join(inherent_concepts)
    # enriched_concepts = ' '.join(enriched_concepts)
    # print("************************************")
    return inherent_concepts


print (enrich_text(u"def estimate_house_sales_price(num_of_bedrooms, sqft, neighborhood):price = 0\
\
  # a little pinch of this\
  price += num_of_bedrooms * 1.0\
  # and a big pinch of that\
  price += sqft * 1.0\
  # maybe a handful of this\
  price += neighborhood * 1.0\
\
  # and finally, just a little extra salt for good measure \
  price += 1.0\
"
                   )
       )
