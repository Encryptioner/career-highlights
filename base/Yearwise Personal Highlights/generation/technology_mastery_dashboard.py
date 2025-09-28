import matplotlib.pyplot as plt
import pandas as pd
import json
from math import pi
import seaborn as sns

# Load the enhanced data
file_path = "../../Yearwise Highlights in ND/graphical/diagram_ready_data.json"
with open(file_path, "r") as f:
    data = json.load(f)

# Create figure with subplots for technology insights
fig = plt.figure(figsize=(20, 14))
gs = fig.add_gridspec(2, 3, height_ratios=[1, 1], width_ratios=[1, 1, 1], hspace=0.3, wspace=0.3)

# 1. Technology Mastery Radar Chart
ax1 = fig.add_subplot(gs[0, 0], projection='polar')

tech_mastery = data["technology_mastery"]
tech_df = pd.DataFrame(tech_mastery).T
tech_df = tech_df.sort_values('proficiency', ascending=False).head(8)  # Top 8 technologies

categories = list(tech_df.index)
proficiency = tech_df['proficiency'].tolist()
years_exp = tech_df['years'].tolist()

# Number of variables
N = len(categories)

# Compute angle for each axis
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]  # Complete the circle

# Close the plot
proficiency += proficiency[:1]
years_exp += years_exp[:1]

# Plot
ax1.set_theta_offset(pi / 2)
ax1.set_theta_direction(-1)

# Draw the proficiency radar
ax1.plot(angles, proficiency, 'o-', linewidth=3, label='Proficiency (1-10)', color='#E74C3C', markersize=8)
ax1.fill(angles, proficiency, alpha=0.25, color='#E74C3C')

# Draw the years experience radar
normalized_years = [(year/max(tech_df['years']))*10 for year in years_exp[:-1]] + [(years_exp[-1]/max(tech_df['years']))*10]
ax1.plot(angles, normalized_years, 'o-', linewidth=3, label='Years Experience (normalized)', color='#3498DB', markersize=8)
ax1.fill(angles, normalized_years, alpha=0.25, color='#3498DB')

# Add category labels
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=11, fontweight='bold')

# Add concentric circles and labels
ax1.set_ylim(0, 10)
ax1.set_yticks([2, 4, 6, 8, 10])
ax1.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=9)
ax1.grid(True, alpha=0.3)

ax1.set_title("Technology Mastery Radar\n(Top 8 Technologies)", fontsize=14, fontweight='bold', color='#2C3E50', pad=20)
ax1.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# 2. Technology Evolution Heatmap
ax2 = fig.add_subplot(gs[0, 1])

tech_evolution = data["technology_evolution"]
skills_by_year = data["skills_by_year"]

# Create a matrix for the heatmap
years = list(skills_by_year.keys())
all_skills = []
for year_skills in skills_by_year.values():
    all_skills.extend(year_skills)
unique_skills = list(set(all_skills))

# Create matrix
matrix = []
for skill in unique_skills[:15]:  # Top 15 skills
    skill_years = []
    for year in years:
        if skill in skills_by_year[year]:
            skill_years.append(1)
        else:
            skill_years.append(0)
    matrix.append(skill_years)

# Create heatmap
sns.heatmap(matrix, xticklabels=years, yticklabels=unique_skills[:15],
            cmap='YlOrRd', cbar_kws={'label': 'Skill Active'},
            ax=ax2, square=False, linewidths=0.5)

ax2.set_title("Skills Evolution Timeline", fontsize=14, fontweight='bold', color='#2C3E50')
ax2.set_xlabel("Year", fontsize=12, fontweight='bold')
ax2.set_ylabel("Skills", fontsize=12, fontweight='bold')

# 3. Project Categories Sunburst (Donut Chart)
ax3 = fig.add_subplot(gs[0, 2])

project_categories = data["project_categories"]
categories = list(project_categories.keys())
counts = [project_categories[cat]["count"] for cat in categories]
colors = [project_categories[cat]["color"] for cat in categories]
complexities = [project_categories[cat]["complexity"] for cat in categories]

# Create nested donut chart
# Outer ring - project counts
wedges1, texts1, autotexts1 = ax3.pie(counts, labels=None, colors=colors, autopct='%1.0f',
                                       radius=1, startangle=90, pctdistance=0.85,
                                       textprops={'fontsize': 10, 'fontweight': 'bold'})

# Inner ring - complexity
inner_colors = ['#2C3E50' if comp > 4.0 else '#34495E' if comp > 3.5 else '#7F8C8D' for comp in complexities]
wedges2, texts2 = ax3.pie(complexities, labels=None, colors=inner_colors,
                         radius=0.6, startangle=90)

# Add center circle
centre_circle = plt.Circle((0,0), 0.3, fc='white', linewidth=2, edgecolor='#2C3E50')
ax3.add_artist(centre_circle)

ax3.set_title("Project Categories Distribution\n(Count & Complexity)", fontsize=14, fontweight='bold', color='#2C3E50')

# Create custom legend
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[i],
                              markersize=10, label=f"{categories[i][:20]}")
                   for i in range(len(categories))]
ax3.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9)

# 4. Industry Impact Bar Chart
ax4 = fig.add_subplot(gs[1, 0])

industry_impact = data["industry_impact"]
industries = list(industry_impact.keys())
impacts = list(industry_impact.values())

bars = ax4.barh(industries, impacts, color=data["visualization_config"]["primary_colors"][:len(industries)],
                alpha=0.8, edgecolor='white', linewidth=2)

# Add value labels on bars
for i, (bar, impact) in enumerate(zip(bars, impacts)):
    ax4.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
             str(impact), va='center', fontsize=11, fontweight='bold')

ax4.set_title("Industry Impact Distribution", fontsize=14, fontweight='bold', color='#2C3E50')
ax4.set_xlabel("Number of Projects", fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3, axis='x')
ax4.set_facecolor('#FAFAFA')

# 5. Complexity Distribution Pie Chart
ax5 = fig.add_subplot(gs[1, 1])

complexity_dist = data["complexity_distribution"]
complexity_levels = list(complexity_dist.keys())
complexity_counts = [complexity_dist[level]["count"] for level in complexity_levels]
complexity_colors = ['#E74C3C', '#F39C12', '#F1C40F', '#27AE60', '#8E44AD']

wedges, texts, autotexts = ax5.pie(complexity_counts, labels=complexity_levels,
                                   colors=complexity_colors, autopct='%1.1f%%',
                                   startangle=90, textprops={'fontsize': 10})

ax5.set_title("Project Complexity Distribution", fontsize=14, fontweight='bold', color='#2C3E50')

# 6. Leadership Metrics
ax6 = fig.add_subplot(gs[1, 2])

leadership_metrics = data["leadership_metrics"]
metrics = list(leadership_metrics.keys())
values = list(leadership_metrics.values())

# Convert to more readable labels
readable_labels = {
    'interns_trained': 'Interns\nTrained',
    'technical_sessions': 'Technical\nSessions',
    'project_proposals': 'Project\nProposals',
    'years_of_mentorship': 'Years of\nMentorship',
    'cross_functional_projects': 'Cross-functional\nProjects'
}
labels = [readable_labels[metric] for metric in metrics]

bars = ax6.bar(labels, values, color=data["visualization_config"]["primary_colors"][:len(values)],
               alpha=0.8, edgecolor='white', linewidth=2)

# Add value labels on bars
for bar, value in zip(bars, values):
    ax6.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             str(value), ha='center', va='bottom', fontsize=12, fontweight='bold')

ax6.set_title("Leadership & Mentorship Metrics", fontsize=14, fontweight='bold', color='#2C3E50')
ax6.set_ylabel("Count", fontsize=12, fontweight='bold')
ax6.grid(True, alpha=0.3, axis='y')
ax6.set_facecolor('#FAFAFA')

# Overall styling
fig.suptitle("Technology Mastery & Impact Analysis Dashboard",
             fontsize=24, fontweight='bold', color='#2C3E50', y=0.98)

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Yearwise Personal Highlights",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

plt.tight_layout()

# Save the technology radar
output_path = "../visual/technology_mastery_dashboard.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print(f"Technology mastery dashboard saved to: {output_path}")