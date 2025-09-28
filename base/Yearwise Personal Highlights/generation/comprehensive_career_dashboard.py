import matplotlib.pyplot as plt
import pandas as pd
import json
import numpy as np
from math import pi
import seaborn as sns
from matplotlib.patches import Rectangle, Circle
import matplotlib.gridspec as gridspec

# Set style
plt.style.use('default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

# Load the enhanced data
file_path = "../../Yearwise Highlights in ND/graphical/diagram_ready_data.json"
with open(file_path, "r") as f:
    data = json.load(f)

# Create the comprehensive dashboard
fig = plt.figure(figsize=(24, 16))

# Create a complex grid layout with more top margin for title
gs_main = gridspec.GridSpec(4, 4, figure=fig, hspace=0.4, wspace=0.3,
                           height_ratios=[1, 0.8, 0.8, 0.6], width_ratios=[1, 1, 1, 1],
                           top=0.90)

# Define color scheme
colors = data["visualization_config"]["primary_colors"]
bg_color = '#FAFAFA'

# 1. Main Career Timeline (Top Section - Full Width)
ax_main = fig.add_subplot(gs_main[0, :])

timeline = data["career_timeline"]
df = pd.DataFrame(timeline)

# Create gradient background for main timeline
gradient = np.linspace(0, 1, 256).reshape(1, -1)
ax_main.imshow(gradient, extent=[2018.5, 2025.5, 0, 12], aspect='auto', cmap='viridis', alpha=0.05)

# Plot projects with enhanced styling
bars = ax_main.bar(df["year"], df["projects"],
                   color=[colors[i % len(colors)] for i in range(len(df))],
                   alpha=0.8, edgecolor='white', linewidth=2, width=0.7)

# Add complexity line
ax_main_twin = ax_main.twinx()
line = ax_main_twin.plot(df["year"], df["complexity"], color='#E74C3C',
                        marker='o', linewidth=4, markersize=12,
                        markerfacecolor='white', markeredgecolor='#E74C3C',
                        markeredgewidth=3, label="Complexity", zorder=10)

# Add focus annotations
for i, row in df.iterrows():
    ax_main.text(row["year"], row["projects"] + 0.5, row["focus"],
                ha="center", va="bottom", fontsize=11, fontweight='bold',
                rotation=45, color='#2C3E50',
                bbox=dict(boxstyle="round,pad=0.4", facecolor='white', alpha=0.9,
                         edgecolor=colors[i % len(colors)], linewidth=2))

# Style main timeline
ax_main.set_xlabel("Year", fontsize=14, fontweight='bold')
ax_main.set_ylabel("Projects Count", fontsize=14, fontweight='bold')
ax_main_twin.set_ylabel("Complexity Level", fontsize=14, fontweight='bold', color='#E74C3C')
ax_main.grid(True, alpha=0.3)
ax_main.set_facecolor(bg_color)
ax_main.set_xlim(2018.5, 2025.5)

# 2. Technology Mastery Radar (Top Left of Second Row)
ax_radar = fig.add_subplot(gs_main[1, 0], projection='polar')

tech_mastery = data["technology_mastery"]
tech_df = pd.DataFrame(tech_mastery).T
tech_df = tech_df.sort_values('proficiency', ascending=False).head(8)

categories = list(tech_df.index)
proficiency = tech_df['proficiency'].tolist()
N = len(categories)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
proficiency += proficiency[:1]

ax_radar.plot(angles, proficiency, 'o-', linewidth=3, color='#E74C3C', markersize=8)
ax_radar.fill(angles, proficiency, alpha=0.25, color='#E74C3C')
ax_radar.set_xticks(angles[:-1])
ax_radar.set_xticklabels(categories, fontsize=10, fontweight='bold')
ax_radar.set_ylim(0, 10)
ax_radar.set_title("Technology Mastery\n(Top 8 Skills)", fontsize=14, fontweight='bold',
                   color='#2C3E50', pad=20)
ax_radar.grid(True, alpha=0.3)

# 3. User Scale Impact (Top Center)
ax_users = fig.add_subplot(gs_main[1, 1])

user_years = df["year"].tolist()
user_counts = df["users"].tolist()
user_colors = ['#3498DB' if users > 50000 else '#F39C12' if users > 0 else '#BDC3C7'
               for users in user_counts]

bars_users = ax_users.bar(user_years, user_counts, color=user_colors,
                         alpha=0.8, edgecolor='white', linewidth=2)

# Add milestone annotations
milestones = data["user_scale_milestones"]
for milestone in milestones:
    if milestone["users"] > 0:
        ax_users.annotate(milestone["milestone"],
                         xy=(milestone["year"], milestone["users"]),
                         xytext=(milestone["year"], milestone["users"] + 30000),
                         ha='center', fontsize=9, fontweight='bold',
                         bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8),
                         arrowprops=dict(arrowstyle='->', color='#2C3E50'))

ax_users.set_title("User Impact Scale", fontsize=14, fontweight='bold', color='#2C3E50')
ax_users.set_ylabel("Users Reached", fontsize=12, fontweight='bold')
ax_users.grid(True, alpha=0.3)
ax_users.set_facecolor(bg_color)

# Format y-axis labels
ax_users.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K' if x > 0 else '0'))

# 4. Project Categories (Top Right)
ax_categories = fig.add_subplot(gs_main[1, 2])

project_categories = data["project_categories"]
categories = list(project_categories.keys())
counts = [project_categories[cat]["count"] for cat in categories]
cat_colors = [project_categories[cat]["color"] for cat in categories]

# Horizontal bar chart
bars_cat = ax_categories.barh(range(len(categories)), counts,
                             color=cat_colors, alpha=0.8, edgecolor='white', linewidth=1)

# Add icons and values
for i, (bar, cat, count) in enumerate(zip(bars_cat, categories, counts)):
    icon = project_categories[cat]["icon"]
    ax_categories.text(-0.5, i, icon, ha='center', va='center', fontsize=16)
    ax_categories.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                      str(count), va='center', fontsize=11, fontweight='bold')

ax_categories.set_yticks(range(len(categories)))
ax_categories.set_yticklabels([cat.replace(' ', '\n').replace('&', '&\n') for cat in categories],
                             fontsize=9)
ax_categories.set_title("Project Categories", fontsize=14, fontweight='bold', color='#2C3E50')
ax_categories.set_xlabel("Project Count", fontsize=12, fontweight='bold')
ax_categories.grid(True, alpha=0.3, axis='x')
ax_categories.set_facecolor(bg_color)

# 5. Role Progression Timeline (Top Far Right)
ax_roles = fig.add_subplot(gs_main[1, 3])

role_data = data["role_progression"]
role_df = pd.DataFrame(role_data)

# Create timeline visualization
y_pos = 0
role_colors = ['#E74C3C', '#F39C12', '#27AE60']
for i, (_, row) in enumerate(role_df.iterrows()):
    # Draw role period
    rect = Rectangle((0, i*2), row["duration"], 0.8,
                    facecolor=role_colors[i], alpha=0.7, edgecolor='white', linewidth=2)
    ax_roles.add_patch(rect)

    # Add role text
    ax_roles.text(row["duration"]/2, i*2 + 0.4, row["role"],
                 ha='center', va='center', fontsize=10, fontweight='bold', color='white')

ax_roles.set_xlim(0, max(role_df["duration"]) + 0.5)
ax_roles.set_ylim(-0.5, len(role_df)*2)
ax_roles.set_yticks([i*2 + 0.4 for i in range(len(role_df))])
ax_roles.set_yticklabels([row["focus"] for _, row in role_df.iterrows()], fontsize=10)
ax_roles.set_xlabel("Years", fontsize=12, fontweight='bold')
ax_roles.set_title("Role Progression", fontsize=14, fontweight='bold', color='#2C3E50')
ax_roles.grid(True, alpha=0.3, axis='x')
ax_roles.set_facecolor(bg_color)

# 6. Industry Impact (Second Row Left)
ax_industry = fig.add_subplot(gs_main[2, 0])

industry_impact = data["industry_impact"]
industries = list(industry_impact.keys())
impacts = list(industry_impact.values())

# Create bubble chart
bubble_colors = colors[:len(industries)]
bubbles = ax_industry.scatter(range(len(industries)), [1]*len(industries),
                             s=[impact*100 for impact in impacts],
                             c=bubble_colors, alpha=0.7, edgecolors='white', linewidths=2)

# Add labels
for i, (industry, impact) in enumerate(zip(industries, impacts)):
    ax_industry.text(i, 1, str(impact), ha='center', va='center',
                    fontsize=12, fontweight='bold', color='white')
    ax_industry.text(i, 0.7, industry.replace(' ', '\n'), ha='center', va='center',
                    fontsize=9, fontweight='bold')

ax_industry.set_xlim(-0.5, len(industries)-0.5)
ax_industry.set_ylim(0.5, 1.3)
ax_industry.set_title("Industry Impact\n(Bubble Size = Project Count)",
                     fontsize=14, fontweight='bold', color='#2C3E50')
ax_industry.set_xticks([])
ax_industry.set_yticks([])
ax_industry.set_facecolor(bg_color)

# 7. Skills Evolution Heatmap (Second Row Center)
ax_skills = fig.add_subplot(gs_main[2, 1])

skills_by_year = data["skills_by_year"]
years = list(skills_by_year.keys())
all_skills = []
for year_skills in skills_by_year.values():
    all_skills.extend(year_skills)

# Get top skills
skill_counts = {}
for skill in all_skills:
    skill_counts[skill] = skill_counts.get(skill, 0) + 1

top_skills = sorted(skill_counts.keys(), key=lambda x: skill_counts[x], reverse=True)[:12]

# Create matrix
matrix = []
for skill in top_skills:
    skill_years = []
    for year in years:
        if skill in skills_by_year[year]:
            skill_years.append(1)
        else:
            skill_years.append(0)
    matrix.append(skill_years)

sns.heatmap(matrix, xticklabels=years, yticklabels=top_skills,
           cmap='RdYlBu_r', cbar_kws={'label': 'Skill Active'},
           ax=ax_skills, square=False, linewidths=1, cbar=False)

ax_skills.set_title("Skills Evolution Timeline", fontsize=14, fontweight='bold', color='#2C3E50')
ax_skills.set_xlabel("Year", fontsize=12, fontweight='bold')
ax_skills.tick_params(axis='y', labelsize=9)

# 8. Complexity Distribution (Second Row Right)
ax_complexity = fig.add_subplot(gs_main[2, 2])

complexity_dist = data["complexity_distribution"]
complexity_levels = list(complexity_dist.keys())
complexity_counts = [complexity_dist[level]["count"] for level in complexity_levels]
complexity_colors = ['#95A5A6', '#F39C12', '#F1C40F', '#27AE60', '#8E44AD']

# Create donut chart
wedges, texts, autotexts = ax_complexity.pie(complexity_counts, labels=None,
                                           colors=complexity_colors, autopct='%1.1f%%',
                                           startangle=90, textprops={'fontsize': 10, 'fontweight': 'bold'},
                                           pctdistance=0.85)

# Add center circle
centre_circle = Circle((0,0), 0.4, fc='white', linewidth=2, edgecolor='#2C3E50')
ax_complexity.add_artist(centre_circle)

ax_complexity.set_title("Project Complexity\nDistribution", fontsize=14, fontweight='bold', color='#2C3E50')

# Add legend
legend_labels = [level.split('(')[1].replace(')', '') for level in complexity_levels]
ax_complexity.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)

# 9. Leadership Metrics (Second Row Far Right)
ax_leadership = fig.add_subplot(gs_main[2, 3])

leadership_metrics = data["leadership_metrics"]
metrics = list(leadership_metrics.keys())
values = list(leadership_metrics.values())

# Create radial bar chart
angles_leadership = np.linspace(0, 2*pi, len(metrics), endpoint=False)
ax_leadership = plt.subplot(gs_main[2, 3], projection='polar')

bars_leadership = ax_leadership.bar(angles_leadership, values,
                                   color=colors[:len(values)], alpha=0.8, width=0.8)

ax_leadership.set_xticks(angles_leadership)
readable_labels = [metric.replace('_', '\n').title() for metric in metrics]
ax_leadership.set_xticklabels(readable_labels, fontsize=9, fontweight='bold')
ax_leadership.set_title("Leadership &\nMentorship Metrics", fontsize=14, fontweight='bold',
                       color='#2C3E50', pad=20)

# 10. Innovation Timeline (Bottom Section - Full Width)
ax_innovation = fig.add_subplot(gs_main[3, :])

innovation_milestones = data["innovation_milestones"]
milestone_df = pd.DataFrame(innovation_milestones)

# Create enhanced timeline
timeline_y = 0
for i, (_, row) in enumerate(milestone_df.iterrows()):
    color = colors[i % len(colors)]

    # Draw milestone point
    ax_innovation.scatter(row["year"], timeline_y, s=400, color=color,
                         alpha=0.8, edgecolor='white', linewidth=3, zorder=10)

    # Add milestone text with alternating positions
    y_offset = 0.3 if i % 2 == 0 else -0.3
    ax_innovation.annotate(row["milestone"],
                          xy=(row["year"], timeline_y),
                          xytext=(row["year"], y_offset),
                          ha='center', va='center',
                          fontsize=11, fontweight='bold',
                          bbox=dict(boxstyle="round,pad=0.5", facecolor=color,
                                   alpha=0.8, edgecolor='white', linewidth=2),
                          arrowprops=dict(arrowstyle='->', color=color, lw=2))

# Draw timeline line
ax_innovation.plot([2018.5, 2025.5], [timeline_y, timeline_y],
                  color='#34495E', linewidth=4, alpha=0.7, zorder=5)

ax_innovation.set_xlim(2018.5, 2025.5)
ax_innovation.set_ylim(-0.6, 0.6)
ax_innovation.set_xlabel("Year", fontsize=14, fontweight='bold')
ax_innovation.set_title("Innovation & Achievement Milestones Timeline",
                       fontsize=16, fontweight='bold', color='#2C3E50')
ax_innovation.set_yticks([])
ax_innovation.spines['left'].set_visible(False)
ax_innovation.spines['right'].set_visible(False)
ax_innovation.spines['top'].set_visible(False)
ax_innovation.grid(True, alpha=0.3, axis='x')
ax_innovation.set_facecolor(bg_color)

# Overall title and styling
fig.suptitle("Comprehensive Career Highlights & Technology Mastery Dashboard",
            fontsize=26, fontweight='bold', color='#2C3E50', y=0.95)

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Yearwise Personal Highlights",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

plt.tight_layout()
plt.subplots_adjust(top=0.88)

# Save the integrated dashboard
output_path = "../visual/comprehensive_career_dashboard.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print(f"Comprehensive dashboard saved to: {output_path}")