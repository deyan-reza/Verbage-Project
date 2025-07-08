#Task: Take in a script with 6 people: M1,M2,M3,F1,F2,F3 and determine if Females use more verbs than Males on average and if it is statistically significant. (Given this is a script in which everyone has ~30+ lines)
# Step 1: Import libraries
import pandas as pd
from scipy import stats
# Step 2: Import dataset
verbs = pd.read_csv("common_english_verbs.csv")
verb_List = verbs["Verb"].tolist()
# Step 3: Make 2 lists (male and female)
Males = []
Females = []
# Step 4: Input script
with open("Example.txt") as script:
    for line in script:
# Step 5: Count verbs per line per person and add to corresponding list
        if line.startswith("M"):
            dialogue = line[3:].strip()
            words = dialogue.split()
            verb_count = sum(1 for word in words if word.lower() in verb_List)
            Males.append(verb_count)
        if line.startswith("F"):
            dialogue = line[3:].strip()
            words = dialogue.split()
            verb_count = sum(1 for word in words if word.lower() in verb_List)
            Females.append(verb_count)    
# Step 6: Find average for each group
mean_male = sum(Males) / len(Males)
mean_female = sum(Females) / len(Females)
# Step 7: Find sample variances
n_male = len(Males)
n_female = len(Females)
var_male = sum((x - mean_male) ** 2 for x in Males) / (n_male - 1)
var_female = sum((x - mean_female) ** 2 for x in Females) / (n_female - 1)
# Step 8: Degrees of Freedom
num = (var_male / n_male + var_female / n_female) ** 2
denom = ((var_male ** 2) / ((n_male ** 2) * (n_male - 1))) + ((var_female ** 2) / ((n_female ** 2) * (n_female - 1)))
df = num / denom
# Step 9: Conduct Welchs t-test
t_stat = (mean_male - mean_female) / ((var_male / n_male + var_female / n_female) ** 0.5)
p_value = 2 * stats.t.sf(abs(t_stat), df)
# Step 10: Output
if p_value < 0.05:
    print("Result is statistically significant at the 0.05 level.")
else:
    print("Result is NOT statistically significant at the 0.05 level.")