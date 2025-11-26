# With reference to Table , obtain the Frequency table for the
# attribute age. From the frequency table you have obtained, calculate the
# information gain of the frequency table while splitting on Age. (Use step
# by step Python/Pandas commands)



import pandas as pd
import math

# 1. Create the dataset (rows taken from the table in the image)
data = [
    {"Age":"Young","Income":"High","Married":"No","Health":"Fair","Class":"No"},
    {"Age":"Young","Income":"High","Married":"No","Health":"Good","Class":"No"},
    {"Age":"Middle","Income":"High","Married":"No","Health":"Fair","Class":"Yes"},
    {"Age":"Old","Income":"Medium","Married":"No","Health":"Fair","Class":"Yes"},
    {"Age":"Old","Income":"Low","Married":"Yes","Health":"Fair","Class":"Yes"},
    {"Age":"Old","Income":"Low","Married":"Yes","Health":"Good","Class":"No"},
    {"Age":"Middle","Income":"Low","Married":"Yes","Health":"Good","Class":"Yes"},
    {"Age":"Young","Income":"Medium","Married":"No","Health":"Fair","Class":"No"},
    {"Age":"Young","Income":"Low","Married":"Yes","Health":"Fair","Class":"Yes"},
    {"Age":"Old","Income":"Medium","Married":"Yes","Health":"Fair","Class":"Yes"},
    {"Age":"Young","Income":"Medium","Married":"Yes","Health":"Good","Class":"Yes"},
    {"Age":"Middle","Income":"Medium","Married":"No","Health":"Good","Class":"Yes"},
    {"Age":"Middle","Income":"High","Married":"Yes","Health":"Fair","Class":"Yes"},
    {"Age":"Old","Income":"Medium","Married":"No","Health":"Good","Class":"No"},
]

df = pd.DataFrame(data)
df['Age'] = df['Age'].str.capitalize()   # normalize capitalization

# 2. Frequency table (Age vs Class)
freq = pd.crosstab(df['Age'], df['Class'])
print("Frequency table (Age x Class):")
print(freq)

# 3. Compute base entropy H(Class)
def entropy(p_list):
    e = 0.0
    for p in p_list:
        if p>0:
            e -= p * math.log2(p)
    return e

total = len(df)
count_yes = (df['Class'] == 'Yes').sum()
count_no  = (df['Class'] == 'No').sum()
p_yes = count_yes / total
p_no  = count_no  / total
base_entropy = entropy([p_yes, p_no])
print(f"\nBase entropy H(Class) = {base_entropy:.6f}  (Yes={count_yes}, No={count_no}, total={total})")

# 4. Compute conditional entropy H(Class | Age)
cond_entropy = 0.0
print("\nEntropy per Age group:")
for age, group in df.groupby('Age'):
    n = len(group)
    cy = (group['Class']=='Yes').sum()
    cn = (group['Class']=='No').sum()
    py = cy / n
    pn = cn / n
    h_age = entropy([py, pn])
    cond_entropy += (n/total) * h_age
    print(f"  {age}: n={n}, Yes={cy}, No={cn}, H = {h_age:.6f}")

# 5. Information gain
info_gain = base_entropy - cond_entropy
print(f"\nConditional entropy H(Class|Age) = {cond_entropy:.6f}")
print(f"Information Gain for split on Age = {info_gain:.6f} bits")
