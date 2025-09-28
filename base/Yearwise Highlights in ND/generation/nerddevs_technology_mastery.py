import matplotlib.pyplot as plt
import pandas as pd
import json
import numpy as np
from math import pi
import seaborn as sns

# Set style
plt.style.use('default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

# Load the ND career data
file_path = "../graphical/diagram_ready_data.json"
with open(file_path, "r") as f:
    data = json.load(f)

# Create figure for technology mastery analysis
fig = plt.figure(figsize=(20, 14))
gs = fig.add_gridspec(3, 3, height_ratios=[1.2, 1, 0.8], width_ratios=[1, 1, 1], hspace=0.35, wspace=0.25)

# Define Nerddevs color scheme
colors = data["visualization_config"]["primary_colors"]
nerddevs_primary = '#FF6B6B'
nerddevs_secondary = '#4ECDC4'
bg_color = '#FAFAFA'

# 1. Technology Mastery Radar Chart (Top Left)
ax1 = fig.add_subplot(gs[0, 0], projection='polar')

tech_mastery = data["technology_mastery"]
tech_df = pd.DataFrame(tech_mastery).T
tech_df = tech_df.sort_values('proficiency', ascending=False).head(10)  # Top 10 technologies

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
years_normalized = [(year/max(tech_df['years']))*10 for year in years_exp] + [(years_exp[0]/max(tech_df['years']))*10]

# Plot proficiency radar
ax1.plot(angles, proficiency, 'o-', linewidth=4, label='Proficiency (1-10)',
         color=nerddevs_primary, markersize=10, markerfacecolor='white',
         markeredgecolor=nerddevs_primary, markeredgewidth=2)
ax1.fill(angles, proficiency, alpha=0.25, color=nerddevs_primary)

# Plot years experience radar
ax1.plot(angles, years_normalized, 'o-', linewidth=3, label='Experience (normalized)',
         color=nerddevs_secondary, markersize=8, markerfacecolor='white',
         markeredgecolor=nerddevs_secondary, markeredgewidth=2)
ax1.fill(angles, years_normalized, alpha=0.15, color=nerddevs_secondary)

# Customize radar chart
ax1.set_theta_offset(pi / 2)
ax1.set_theta_direction(-1)
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=11, fontweight='bold')
ax1.set_ylim(0, 10)
ax1.set_yticks([2, 4, 6, 8, 10])
ax1.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=9, alpha=0.7)
ax1.grid(True, alpha=0.3)

ax1.set_title("Technology Mastery Overview\n(Top 10 Skills at Nerddevs)",
              fontsize=14, fontweight='bold', color='#2C3E50', pad=25)
ax1.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# 2. Technology Evolution Timeline (Top Center)
ax2 = fig.add_subplot(gs[0, 1])

tech_evolution = data["technology_evolution"]

# Create flow chart for technology evolution
y_start = len(tech_evolution) - 1
for i, tech_cat in enumerate(tech_evolution):
    category = tech_cat["category"]
    progression = tech_cat["progression"]

    # Draw category label
    ax2.text(-0.5, y_start - i, category, ha='right', va='center',
            fontsize=11, fontweight='bold', color='#2C3E50')

    # Draw progression flow
    for j, tech in enumerate(progression):
        # Technology box
        width = min(len(tech) * 0.08, 1.5)  # Adaptive width based on text length
        rect = plt.Rectangle((j*2, y_start - i - 0.3), width, 0.6,
                           facecolor=colors[j % len(colors)], alpha=0.8,
                           edgecolor='white', linewidth=2)
        ax2.add_patch(rect)

        # Technology text
        ax2.text(j*2 + width/2, y_start - i, tech, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white', wrap=True)

        # Arrow to next technology
        if j < len(progression) - 1:
            ax2.arrow(j*2 + width + 0.1, y_start - i, 0.6, 0,
                     head_width=0.15, head_length=0.1,
                     fc='#2C3E50', ec='#2C3E50', alpha=0.7)

ax2.set_xlim(-1, 8)
ax2.set_ylim(-0.8, len(tech_evolution))
ax2.set_title("Technology Stack Evolution at Nerddevs\n(Skill Progression Over Time)",
              fontsize=14, fontweight='bold', color='#2C3E50')
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_facecolor(bg_color)

# 3. Skills Heatmap by Year (Top Right)
ax3 = fig.add_subplot(gs[0, 2])

skills_by_year = data["skills_by_year"]
years = list(skills_by_year.keys())
all_skills = []

for year_skills in skills_by_year.values():
    all_skills.extend(year_skills)

# Get most frequent skills
skill_counts = {}
for skill in all_skills:
    skill_counts[skill] = skill_counts.get(skill, 0) + 1

top_skills = sorted(skill_counts.keys(), key=lambda x: skill_counts[x], reverse=True)[:15]

# Create matrix for heatmap
matrix = []
for skill in top_skills:
    skill_years = []
    for year in years:
        if skill in skills_by_year[year]:
            skill_years.append(1)
        else:
            skill_years.append(0)
    matrix.append(skill_years)

# Create custom colormap for Nerddevs theme
colors_heatmap = ['white', nerddevs_primary]
from matplotlib.colors import ListedColormap
cmap = ListedColormap(colors_heatmap)

sns.heatmap(matrix, xticklabels=years, yticklabels=top_skills,
           cmap=cmap, cbar_kws={'label': 'Skill Active'},
           ax=ax3, square=False, linewidths=1.5, linecolor='white')

ax3.set_title("Skills Evolution Heatmap\n(Year-by-Year Development)",
              fontsize=14, fontweight='bold', color='#2C3E50')
ax3.set_xlabel("Year", fontsize=12, fontweight='bold')
ax3.tick_params(axis='y', labelsize=9)
ax3.tick_params(axis='x', rotation=0)

# 4. Project Categories with Complexity (Middle Left)
ax4 = fig.add_subplot(gs[1, 0])

project_categories = data["project_categories"]
categories = list(project_categories.keys())
counts = [project_categories[cat]["count"] for cat in categories]
complexities = [project_categories[cat]["complexity"] for cat in categories]
cat_colors = [project_categories[cat]["color"] for cat in categories]

# Create bubble chart
x_pos = counts
y_pos = complexities
sizes = [count * 50 for count in counts]  # Scale bubble size

bubbles = ax4.scatter(x_pos, y_pos, s=sizes, c=cat_colors, alpha=0.7,
                     edgecolors='white', linewidths=2)

# Add category labels
for i, (cat, count, complexity) in enumerate(zip(categories, counts, complexities)):
    # Shorten long category names
    short_cat = cat[:20] + "..." if len(cat) > 20 else cat
    ax4.annotate(short_cat, (count, complexity),
                xytext=(5, 5), textcoords='offset points',
                fontsize=9, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=cat_colors[i], alpha=0.7),
                color='white')

ax4.set_xlabel("Number of Projects", fontsize=12, fontweight='bold')
ax4.set_ylabel("Average Complexity Level", fontsize=12, fontweight='bold')
ax4.set_title("Project Categories: Count vs Complexity\n(Bubble Size = Project Count)",
              fontsize=14, fontweight='bold', color='#2C3E50')
ax4.grid(True, alpha=0.3)
ax4.set_facecolor(bg_color)

# 5. Industry Impact Distribution (Middle Center)
ax5 = fig.add_subplot(gs[1, 1])

industry_impact = data["industry_impact"]
industries = list(industry_impact.keys())
impacts = list(industry_impact.values())

# Create horizontal bar chart with gradient effect
bars = ax5.barh(industries, impacts, color=colors[:len(industries)],
               alpha=0.8, edgecolor='white', linewidth=2)

# Add value labels
for i, (bar, impact) in enumerate(zip(bars, impacts)):
    ax5.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            str(impact), va='center', fontsize=11, fontweight='bold')

# Add icons (simplified as text)
industry_icons = {'Government Solutions': '🏛️', 'Educational Technology': '🎓',
                  'Financial Technology': '💰', 'Artificial Intelligence': '🤖',
                  'E-Commerce': '🛒', 'Mobile Technology': '📱'}

for i, (industry, impact) in enumerate(zip(industries, impacts)):
    icon = industry_icons.get(industry, '🔧')
    ax5.text(-0.5, i, icon, ha='center', va='center', fontsize=16)

ax5.set_title("Industry Impact Distribution\n(Project Count by Sector)",
              fontsize=14, fontweight='bold', color='#2C3E50')
ax5.set_xlabel("Number of Projects", fontsize=12, fontweight='bold')
ax5.grid(True, alpha=0.3, axis='x')
ax5.set_facecolor(bg_color)

# 6. Leadership & Mentorship Growth (Middle Right)
ax6 = fig.add_subplot(gs[1, 2])

leadership_metrics = data["leadership_metrics"]
metrics = list(leadership_metrics.keys())
values = list(leadership_metrics.values())

# Create radial bar chart
angles_leadership = np.linspace(0, 2*pi, len(metrics), endpoint=False)
ax6 = plt.subplot(gs[1, 2], projection='polar')

bars = ax6.bar(angles_leadership, values, width=0.8, alpha=0.8,
              color=colors[:len(values)], edgecolor='white', linewidth=2)

# Customize radial chart
ax6.set_xticks(angles_leadership)
readable_labels = [metric.replace('_', '\n').title() for metric in metrics]
ax6.set_xticklabels(readable_labels, fontsize=10, fontweight='bold')
ax6.set_ylim(0, max(values) + 2)
ax6.set_title("Leadership & Mentorship\nMetrics Overview", fontsize=14, fontweight='bold',
              color='#2C3E50', pad=25)
ax6.grid(True, alpha=0.3)

# 7. Complexity Evolution Over Time (Bottom Left)
ax7 = fig.add_subplot(gs[2, 0])

timeline = data["career_timeline"]
df = pd.DataFrame(timeline)

# Create area chart showing complexity growth
ax7.fill_between(df["year"], df["complexity"], alpha=0.4, color=nerddevs_primary, label='Technical Complexity')
ax7.plot(df["year"], df["complexity"], color=nerddevs_primary, linewidth=4,
         marker='D', markersize=10, markerfacecolor='white',
         markeredgecolor=nerddevs_primary, markeredgewidth=3)

# Add complexity level annotations
complexity_levels = {1: 'Basic', 2: 'Foundation', 3: 'Professional', 4: 'Advanced', 5: 'Revolutionary'}
for _, row in df.iterrows():
    level_name = complexity_levels.get(row["complexity"], 'Unknown')
    ax7.annotate(f'Level {row["complexity"]}\n{level_name}',
                xy=(row["year"], row["complexity"]),
                xytext=(0, 20), textcoords='offset points',
                ha='center', fontsize=9, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=nerddevs_secondary, alpha=0.8),
                arrowprops=dict(arrowstyle='->', color=nerddevs_primary))

ax7.set_title("Technical Complexity Evolution\n(Skill Level Growth)",
              fontsize=14, fontweight='bold', color='#2C3E50')
ax7.set_xlabel("Year", fontsize=12, fontweight='bold')
ax7.set_ylabel("Complexity Level", fontsize=12, fontweight='bold')
ax7.grid(True, alpha=0.3)
ax7.set_facecolor(bg_color)
ax7.set_ylim(0, 6)

# 8. Technology Proficiency Distribution (Bottom Center)
ax8 = fig.add_subplot(gs[2, 1])

# Get proficiency distribution
proficiencies = list(tech_mastery.values())
proficiency_levels = [tech['proficiency'] for tech in proficiencies]

# Create histogram
bins = range(1, 11)
counts, bins, patches = ax8.hist(proficiency_levels, bins=bins, alpha=0.8,
                                color=nerddevs_primary, edgecolor='white', linewidth=2)

# Color bars based on proficiency level
for i, (count, patch) in enumerate(zip(counts, patches)):
    if i < 3:  # Low proficiency (1-3)
        patch.set_facecolor('#95A5A6')
    elif i < 6:  # Medium proficiency (4-6)
        patch.set_facecolor('#F39C12')
    else:  # High proficiency (7-10)
        patch.set_facecolor(nerddevs_primary)

ax8.set_title("Technology Proficiency\nDistribution", fontsize=14, fontweight='bold', color='#2C3E50')
ax8.set_xlabel("Proficiency Level", fontsize=12, fontweight='bold')
ax8.set_ylabel("Number of Technologies", fontsize=12, fontweight='bold')
ax8.grid(True, alpha=0.3, axis='y')
ax8.set_facecolor(bg_color)

# 9. Recent Technology Adoption (Bottom Right)
ax9 = fig.add_subplot(gs[2, 2])

# Focus on 2024-2025 skills
recent_years = ['2024', '2025']
recent_skills = []
for year in recent_years:
    recent_skills.extend(skills_by_year.get(year, []))

# Count recent skill mentions
recent_skill_counts = {}
for skill in recent_skills:
    recent_skill_counts[skill] = recent_skill_counts.get(skill, 0) + 1

# Get top recent skills
top_recent = sorted(recent_skill_counts.items(), key=lambda x: x[1], reverse=True)[:8]
skills, skill_counts = zip(*top_recent)

# Create horizontal bar chart for recent skills
bars = ax9.barh(range(len(skills)), skill_counts,
               color=[nerddevs_primary if 'AI' in skill or 'Real-time' in skill
                      else nerddevs_secondary for skill in skills],
               alpha=0.8, edgecolor='white', linewidth=2)

ax9.set_yticks(range(len(skills)))
ax9.set_yticklabels(skills, fontsize=10, fontweight='bold')
ax9.set_title("Recent Technology Focus\n(2024-2025 Highlights)",
              fontsize=14, fontweight='bold', color='#2C3E50')
ax9.set_xlabel("Skill Mentions", fontsize=12, fontweight='bold')
ax9.grid(True, alpha=0.3, axis='x')
ax9.set_facecolor(bg_color)

# Overall styling and title
fig.suptitle("Nerddevs Technology Mastery & Skills Development Analysis\nComprehensive Technical Growth Visualization (2019-2025)",
            fontsize=22, fontweight='bold', color='#2C3E50', y=0.98)

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Yearwise Highlights in ND",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

plt.tight_layout()

# Save the technology mastery dashboard
output_path = "../visual/nerddevs_technology_mastery.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print(f"Nerddevs technology mastery dashboard saved to: {output_path}")