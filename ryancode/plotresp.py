'''

'''

Is = [1,2,3,4,5]
Qs = [6,7,8,9,10]

def plot_resp(I_arr, Q_arr, indexes):

	index1 = False		#if there is only 1 index

	if len(indexes) > 1:	
		index1 = False

	if index1 == True:
		#plot the range of indexes 
		low = indexes[0]
		max = len(indexes) - 1
		upper = indexes[max]
		#there is more code here that I think that I am missing??	
	if index1 == False:
		point = indexes[0]
		plt.plot(I_arr[point], Q_arr[point]);
		plt.show()

ind = [1]
plot_resp(Is, Qs, ind)
