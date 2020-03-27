# Installed pgmpy if not installed
conda install -c ankurankan pgmpy

#import TabularCPP
from pgmpy.factors.discrete import TabularCPD

# This example shows the performance of top MBA graduates fund manages with diffrent programs
# Where MarketPerformace_0 and Program_0 shows the poor performance and MarketPerformace_1, Program_1 shows the high performance

# Now Create a Joint Probability Distribution
cpd = TabularCPD('MarketPerformance',2,[[0.11,0.06],[0.29,0.54]],evidence=['Program'],evidence_card=[2])
print(cpd)

# Sum of the table shows the Marginal Probability and columns in the table shows the Joint Probability.
# We can also find the Conditional Probability Distribution Object of PGMPy

cpd = TabularCPD('grade', 2,
                        [[0.7, 0.6, 0.6, 0.2],[0.3, 0.4, 0.4, 0.8]],
                        evidence = ['intel', 'diff'], evidence_card = [2, 2])
print(cpd.variables)
print(cpd.cardinality)

# Understanding Joint Probability Distribution Object of PGMPy
from pgmpy.factors.discrete import JointProbabilityDistribution as JPD
prob = JPD(['I','D','G'],[2,2,3],
               [0.126,0.168,0.126,0.009,0.045,0.126,0.252,0.0224,0.0056,0.06,0.036,0.024])
prob.check_independence(['I'], ['D'])
prob.check_independence(['I'], ['D'], [('G', 1)])
prob.get_independencies()
