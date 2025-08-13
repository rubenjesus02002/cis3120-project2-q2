import pandas as pd
import matplotlib.pyplot as plt

men_swim   = pd.read_csv("MenSwimming.csv")
women_swim = pd.read_csv("WomenSwimming.csv")
men_vb     = pd.read_csv("MenVolleyball.csv", encoding="latin-1") 
women_vb   = pd.read_csv("WomenVolleyball.csv")

avg_men_swim   = float(men_swim["Height"].mean())
avg_women_swim = float(women_swim["Height"].mean())
avg_men_vb     = float(men_vb["Height"].mean())
avg_women_vb   = float(women_vb["Height"].mean())

# Step 3: Combine for overall swimmer and volleyball averages
swim_all = pd.concat([men_swim[["Height"]], women_swim[["Height"]]])
vb_all   = pd.concat([men_vb[["Height"]],   women_vb[["Height"]]])

avg_swim_all = float(swim_all["Height"].mean())
avg_vb_all   = float(vb_all["Height"].mean())

print("Average Heights:")
print(f"Men's Swimming:      {avg_men_swim}")
print(f"Women's Swimming:    {avg_women_swim}")
print(f"Men's Volleyball:    {avg_men_vb}")
print(f"Women's Volleyball:  {avg_women_vb}")
print("Averages:")
print(f"All Swimmers:        {avg_swim_all}")
print(f"All Volleyball:      {avg_vb_all}")

# Step 5: Print conclusion (Q7)
if avg_swim_all > avg_vb_all:
    print("Conclusion: Swimmers are taller on average in this finding.")
elif avg_swim_all < avg_vb_all:
    print("Conclusion: Volleyball players are taller on average in this finding.")
else:
    print("Conclusion: Same average height in this finding.")

avg_data = {
    'Team': [
        "Men's Swim Team",
        "Women's Swim Team",
        "Men's Volleyball Team",
        "Women's Volleyball Team"
    ],
    'Avg Height': [
        avg_men_swim,
        avg_women_swim,
        avg_men_vb,
        avg_women_vb
    ]
}

avg_data_df = pd.DataFrame(avg_data)

avg_data_df.plot.bar(x="Team", y="Avg Height", title="Avg Heights Among Teams")
plt.ylabel("Height (inches)")
plt.tight_layout()
plt.show()