def training(reviews, univocab, bivocab):
	N = len(reviews)	#	number of reviews
	N1 = 0			#	number of positive reviews
	N2 = 0			#	number of negative reviews
	
	positiveReview = ''	#	super doc for positive reviews
	negativeReview = ''	#	super doc for negative reviews

	for review in reviews:
		if review[0] == '+':
			N1 += 1
			positiveReview += ' ' + review[1:] 
		else:
			N2 += 1
			negativeReview += ' ' + review[1:]
	

	P1 = (1.0 * N1)/N		#	p(+)	
	P2 = (1.0 * N2)/N		#	p(-)	

	positive_Uni_Probabs = []	#	p(word|+)	
	negative_Uni_Probabs = []	#	p(word|-)
	positive_bi_Probabs = []	#	p(word|+)	
	negative_bi_Probabs = []	#	p(word|-)	
	pos_uni_counts = []
	neg_uni_counts = []
	
	totalCountInPositive = 0
	totalCountInNegative = 0

	for word in univocab:
		pos_uni_counts.append(1)
		neg_uni_counts.append(1)

		totalCountInPositive += positiveReview.count(word) + 1
		totalCountInNegative += negativeReview.count(word) + 1

	# for word in univocab:
	# 	positiveCount = positiveReview.count(word) + 1
	# 	positive_Uni_Probabs.append((1.0 * positiveCount)/totalCountInPositive)	#	(count(word in +) + 1) / sum of (count(word' in +) + 1)

	# 	negativeCount = negativeReview.count(word) + 1
	# 	negative_Uni_Probabs.append((1.0 * negativeCount)/totalCountInNegative)	#	(count(word in -) + 1) / sum of (count(word' in -) + 1)


	for word in bivocab:
		w1 = word.split()[0]
		w2 = word.split()[1]
		
		if positiveReview.count(word) == 0:
			pos_uni_counts[univocab.index(w1)] += 1
			pos_uni_counts[univocab.index(w2)] += 1
			positive_bi_Probabs.append(0)
		else:
			positiveCount = positiveReview.count(word)
			positive_bi_Probabs.append( (1.0 * positiveCount)/positiveReview.count(w1) )
		
		if negativeReview.count(word) == 0:
			neg_uni_counts[univocab.index(w1)] += 1
			neg_uni_counts[univocab.index(w2)] += 1
			negative_bi_Probabs.append(0)
		else:
			negativeCount = negativeReview.count(word) 
			negative_bi_Probabs.append( (1.0 * negativeCount)/negativeReview.count(w1) )


	for i in range(len(univocab)):
		positive_Uni_Probabs.append((1.0 * pos_uni_counts[i])/totalCountInPositive)	#	here (count(word in +) + 1) / sum of (count(word' in +) + 1)
		negative_Uni_Probabs.append((1.0 * neg_uni_counts[i])/totalCountInNegative)	#	here (count(word in -) + 1) / sum of (count(word' in -) + 1)

	
	return (P1, P2, positive_Uni_Probabs, negative_Uni_Probabs, positive_bi_Probabs, negative_bi_Probabs)

if __name__ == '__main__':
	data = open("new_data.txt", "r")
	file1 = open("unigram.txt", "r")
	file2 = open("bigram.txt", "r")

	review = data.read().splitlines()
	univocab = file1.read().splitlines()
	bivocab = file2.read().splitlines()

	val = training(review, univocab, bivocab)
	print val[0], val[1], val[2], val[3], val[4], val[5]
	print len(val[2]), len(val[3]), len(val[4]), len(val[5])
