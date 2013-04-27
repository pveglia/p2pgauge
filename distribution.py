class Distribution:
	"given a dictionary that contains the bins it calculates PDF and CDF"

	def PDF(self,dictionary):
	
		# convert the dictionary into a list
		pdfList = []
		for elem in dictionary.iteritems():
			# elem[0] is the axis and elem[1] is the value
			obj = [elem[0], elem[1]] 
			pdfList.append(obj)


		# sorting of the list based upon the first elem of each object
		pdfList.sort()

		# calculate the sum of all values
		tot = 0.0
		for elem in pdfList:
			tot += float(elem[1]) # add evry value

		# normalize each element of the list and put them in a new list
		pdf = []
		if tot != 0:
			for elem in pdfList:
				elem[1] = float(elem[1]) / float(tot)
				pdf.append(elem)
	

		return pdf

	def CDF(self,pdf):
		cdf = []
		prec = 0
		for elem in pdf:
			newElem = [elem[0], elem[1] + prec]
			prec = elem[1] + prec
			cdf.append(newElem)
		return cdf

	def writeOnFile(self,filename,pdfList):
		pdf_file = open(filename,"w")
		
		for elem in pdfList:
			if elem[1] > 0:
				pdf_file.write(str(elem[0]) + ' ' + str(elem[1]) + '\n')
		
		pdf_file.close()

