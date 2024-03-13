from scipy import special
import numpy 
import pandas
import matplotlib.pyplot as plt

# Define inputs 
numFeatures = 7
numSampledpRun = 5
numRuns = 10000
numTimesEachFeatureSampled = 1000 
numSimulationRuns = 1000

# Simulate feature vector 
featureVector = pandas.DataFrame(range(0,numFeatures))
featureVector = featureVector.transpose()
TimesToFullySample = numpy.zeros(numSimulationRuns)

# Sample feature vector 
for ii in range(numSimulationRuns):
    print(ii)
    numTimesSampled = numpy.zeros(numFeatures) 

    for jj in range(numRuns):
        thisRunsSample = featureVector.sample(n=numSampledpRun,axis='columns')
        maxKK = len(thisRunsSample.axes[1])

        for kk in range(0, maxKK): 
            sampledValue = thisRunsSample.iloc[0, kk]
            numTimesSampled[sampledValue] = numTimesSampled[sampledValue] + 1
        
        if (min(numTimesSampled) == float(numTimesEachFeatureSampled)): 
            TimesToFullySample[ii] = jj 
            ii = ii + 1
            break

print(TimesToFullySample)  
plt.hist(TimesToFullySample)
plt.show()   













# Code adapted from https://www.johndcook.com/blog/2022/05/14/exhaustive-sampling/ 

# Function definition for Stirling number of the second order    
#def k_factorial_stirling(n, k):
   # return sum((-1)**i * special.comb(k, i)*(k-i)**n for i in range(k+1))  

#kVal = 17
#nVal = 17
#p = k_factorial_stirling(nVal, kVal) / kVal**kVal

