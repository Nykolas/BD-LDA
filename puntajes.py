import gensim
from gensim.models import CoherenceModel
import matplotlib.pyplot as plt
def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
	"""
	Compute c_v coherence for various number of topics

	Parameters:
	----------
	dictionary : Gensim dictionary
	corpus : Gensim corpus
	texts : List of input texts
	limit : Max num of topics

	Returns:
	-------
	model_list : List of LDA topic models
	coherence_values : Coherence values corresponding to the LDA model with respective number of topics
	"""
	coherence_values = []
	model_list = []
	for num_topics in range(start, limit, step):
		#model = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=num_topics, id2word=id2word)
		model = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, 
				   num_topics=num_topics, random_state=42, 
				   chunksize=200, passes=10, alpha='auto')
		model_list.append(model)
		coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v',processes =1)
		coherence_values.append(coherencemodel.get_coherence())

	return model_list, coherence_values

def graficar_choerencia(dictionary, corpus, texts, limit):
	STEP_CONS = 1
	START_CONS = 3
	model_list, coherence_values = compute_coherence_values(dictionary=dictionary, corpus=corpus, 
				texts=texts, start=START_CONS, limit=limit, step=STEP_CONS)

	limit=limit; start=START_CONS; step=STEP_CONS;
	x = range(start, limit, step)
	plt.plot(x, coherence_values)
	plt.xlabel("Num Topics")
	plt.ylabel("Coherence score")
	plt.legend(("coherence_values"), loc='best')
	plt.show()