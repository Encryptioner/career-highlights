import matplotlib.pyplot as plt
import pandas as pd
import json
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch, Circle

# Set style
plt.style.use('default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

# Load the project data
file_path = "../graphical/diagram_ready_data.json"
with open(file_path, "r") as f:
    data = json.load(f)

# Create innovation timeline figure
fig = plt.figure(figsize=(22, 14))
gs = gridspec.GridSpec(4, 3, figure=fig, height_ratios=[1.2, 0.8, 0.8, 0.8], width_ratios=[1.5, 1, 1], hspace=0.35, wspace=0.3)

# Define color scheme
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FCEA2B', '#FF9F43', '#A29BFE', '#6C5CE7', '#FD79A8', '#00CEC9']
primary_color = '#FF6B6B'
secondary_color = '#4ECDC4'
bg_color = '#FAFAFA'

projects_timeline = data["projects_timeline"]
df = pd.DataFrame(projects_timeline)

# 1. Main Project Timeline (Top Left - Large)
ax1 = fig.add_subplot(gs[0, :2])

# Create gradient background
gradient = np.linspace(0, 1, 256).reshape(256, -1)
gradient = np.vstack((gradient, gradient))
ax1.imshow(gradient, extent=[2015.5, 2025.5, 0, 6], aspect='auto', cmap='viridis', alpha=0.08)

# Create scatter plot with project complexity and categories
categories = df["category"].unique()
category_colors = {cat: colors[i % len(colors)] for i, cat in enumerate(categories)}

for category in categories:
    cat_df = df[df["category"] == category]
    ax1.scatter(cat_df["year"], cat_df["complexity"],
               s=[200 + 50 * comp for comp in cat_df["complexity"]],  # Size based on complexity
               c=[category_colors[category]], alpha=0.7,
               edgecolors='white', linewidths=2, label=category, zorder=10)

# Add project name annotations
for _, row in df.iterrows():
    # Shorten long names
    name = row["name"][:20] + "..." if len(row["name"]) > 20 else row["name"]
    ax1.annotate(name,
                xy=(row["year"], row["complexity"]),
                xytext=(10, 10), textcoords='offset points',
                ha='left', fontsize=8, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=category_colors[row["category"]],
                         alpha=0.8, edgecolor='white'),
                color='white', rotation=15)

# Add development phases
phases = [(2016, 2018, 'Foundation & Learning', secondary_color, 'Phase 1'),
          (2019, 2019, 'Advanced Systems', '#F39C12', 'Phase 2'),
          (2022, 2022, 'Enterprise Architecture', '#9B59B6', 'Phase 3'),
          (2024, 2025, 'Innovation Explosion', primary_color, 'Phase 4')]

for start, end, phase, color, label in phases:
    if start == end:
        ax1.axvline(x=start, color=color, alpha=0.4, linewidth=4, zorder=1)
    else:
        ax1.axvspan(start - 0.4, end + 0.4, alpha=0.15, color=color, zorder=1)

    mid_year = (start + end) / 2
    ax1.text(mid_year, 5.7, f'{label}\n{phase}', ha='center', va='center',
            fontsize=11, fontweight='bold', color=color,
            bbox=dict(boxstyle="round,pad=0.4", facecolor='white', alpha=0.9,
                     edgecolor=color, linewidth=2))

# Styling
ax1.set_title("Personal Projects Innovation Timeline: Technology Evolution & Complexity Growth",
             fontsize=18, fontweight='bold', color='#2C3E50', pad=20)
ax1.set_xlabel("Year", fontsize=14, fontweight='bold')
ax1.set_ylabel("Project Complexity Level", fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_facecolor(bg_color)
ax1.set_xlim(2015.5, 2025.5)
ax1.set_ylim(0, 6)
ax1.legend(loc='upper left', bbox_to_anchor=(0, 1), ncol=2, fontsize=9)

# 2. Technology Stack Evolution (Top Right)
ax2 = fig.add_subplot(gs[0, 2])

tech_languages = data["technology_evolution"]["languages"]

# Create technology progression chart
years_tech = [tech["year"] for tech in tech_languages]
primary_techs = [tech["primary"] for tech in tech_languages]

# Create timeline with technology labels
for i, (year, tech, tech_data) in enumerate(zip(years_tech, primary_techs, tech_languages)):
    # Draw technology circle
    ax2.scatter(0.5, i, s=300, color=colors[i % len(colors)],
               alpha=0.8, edgecolor='white', linewidth=3, zorder=10)

    # Add technology name
    ax2.text(0.8, i, tech, ha='left', va='center',
            fontsize=12, fontweight='bold', color=colors[i % len(colors)])

    # Add year
    ax2.text(0.2, i, str(year), ha='right', va='center',
            fontsize=11, fontweight='bold', color='#7F8C8D')

    # Add focus area
    focus = tech_data["focus"]
    ax2.text(1.5, i, focus[:25] + "..." if len(focus) > 25 else focus,
            ha='left', va='center', fontsize=9, style='italic',
            color='#2C3E50', wrap=True)

# Connect the dots
for i in range(len(years_tech) - 1):
    ax2.plot([0.5, 0.5], [i, i + 1], color='#BDC3C7',
            linewidth=3, alpha=0.7, zorder=5)

ax2.set_xlim(0, 2.5)
ax2.set_ylim(-0.5, len(years_tech))
ax2.set_title("Technology Stack\nEvolution", fontsize=14, fontweight='bold', color='#2C3E50')
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_facecolor(bg_color)

# 3. Project Types by Complexity (Second Row Left)
ax3 = fig.add_subplot(gs[1, 0])

# Group projects by type and calculate average complexity
project_types = df["type"].value_counts()
type_complexity = df.groupby("type")["complexity"].agg(['mean', 'count']).reset_index()

# Create bubble chart
for _, row in type_complexity.iterrows():
    proj_type = row["type"]
    avg_complexity = row["mean"]
    project_count = row["count"]

    # Find color based on first project of this type
    type_color = category_colors[df[df["type"] == proj_type].iloc[0]["category"]]

    ax3.scatter(project_count, avg_complexity, s=project_count * 100,
               color=type_color, alpha=0.7, edgecolor='white', linewidth=2)

    # Add type label
    ax3.annotate(proj_type[:15] + "..." if len(proj_type) > 15 else proj_type,
                xy=(project_count, avg_complexity),
                xytext=(5, 5), textcoords='offset points',
                fontsize=9, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=type_color, alpha=0.8),
                color='white')

ax3.set_title("Project Types by Complexity\n(Bubble Size = Project Count)",
             fontsize=14, fontweight='bold', color='#2C3E50')
ax3.set_xlabel("Number of Projects", fontsize=12, fontweight='bold')
ax3.set_ylabel("Average Complexity", fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.set_facecolor(bg_color)

# 4. Innovation Impact by Year (Second Row Center)
ax4 = fig.add_subplot(gs[1, 1])

innovation_milestones = data["innovation_milestones"]
innovation_df = pd.DataFrame(innovation_milestones)

# Create impact visualization
impact_levels = {"Foundation": 1, "Web Development": 2, "Academic Contribution": 3,
                "Advanced Systems": 4, "Professional Development": 3,
                "Portfolio Excellence": 2, "Revolutionary Innovation": 5}

impact_scores = [impact_levels.get(milestone["impact"], 3) for milestone in innovation_milestones]
years_innovation = [milestone["year"] for milestone in innovation_milestones]

# Create area chart
ax4.fill_between(years_innovation, impact_scores, alpha=0.4, color=primary_color)
ax4.plot(years_innovation, impact_scores, color=primary_color, linewidth=4,
         marker='D', markersize=10, markerfacecolor='white',
         markeredgecolor=primary_color, markeredgewidth=3)

# Add milestone annotations
for i, milestone in enumerate(innovation_milestones):
    ax4.annotate(milestone["milestone"][:20] + "..." if len(milestone["milestone"]) > 20 else milestone["milestone"],
                xy=(milestone["year"], impact_scores[i]),
                xytext=(0, 20 if i % 2 == 0 else -20), textcoords='offset points',
                ha='center', fontsize=9, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=secondary_color, alpha=0.8),
                arrowprops=dict(arrowstyle='->', color=primary_color),
                color='white')

ax4.set_title("Innovation Impact\nProgression", fontsize=14, fontweight='bold', color='#2C3E50')
ax4.set_xlabel("Year", fontsize=12, fontweight='bold')
ax4.set_ylabel("Impact Level", fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3)
ax4.set_facecolor(bg_color)
ax4.set_ylim(0, 6)

# 5. Technology Categories Distribution (Second Row Right)
ax5 = fig.add_subplot(gs[1, 2])

# Count technologies by category
tech_by_category = {}
for _, project in df.iterrows():
    for tech in project["tech"]:
        category = project["category"]
        if category not in tech_by_category:
            tech_by_category[category] = set()
        tech_by_category[category].add(tech)

# Convert to counts
tech_counts = {cat: len(techs) for cat, techs in tech_by_category.items()}
cat_names = list(tech_counts.keys())
counts = list(tech_counts.values())

# Create horizontal bar chart
bars = ax5.barh(range(len(cat_names)), counts,
                color=[category_colors[cat] for cat in cat_names],
                alpha=0.8, edgecolor='white', linewidth=2)

# Add value labels
for i, (bar, count) in enumerate(zip(bars, counts)):
    ax5.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
             str(count), va='center', fontsize=11, fontweight='bold')

ax5.set_yticks(range(len(cat_names)))
ax5.set_yticklabels(cat_names, fontsize=10)
ax5.set_title("Technology Diversity\nby Category", fontsize=14, fontweight='bold', color='#2C3E50')
ax5.set_xlabel("Unique Technologies", fontsize=12, fontweight='bold')
ax5.grid(True, alpha=0.3, axis='x')
ax5.set_facecolor(bg_color)

# 6. Framework Evolution (Third Row Left)
ax6 = fig.add_subplot(gs[2, 0])

frameworks = data["technology_evolution"]["frameworks"]

# Create framework progression
for i, fw_period in enumerate(frameworks):
    period = fw_period["period"]
    frameworks_list = fw_period["frameworks"]
    complexity = fw_period["complexity"]

    # Create box for each framework period
    rect = FancyBboxPatch((i - 0.4, 0), 0.8, len(frameworks_list),
                         boxstyle="round,pad=0.05",
                         facecolor=colors[i % len(colors)], alpha=0.8,
                         edgecolor='white', linewidth=2)
    ax6.add_patch(rect)

    # Add framework names
    for j, framework in enumerate(frameworks_list):
        ax6.text(i, j + 0.5, framework, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white')

    # Add period and complexity labels
    ax6.text(i, -0.5, period, ha='center', va='center',
            fontsize=10, fontweight='bold', color=colors[i % len(colors)])
    ax6.text(i, len(frameworks_list) + 0.3, complexity, ha='center', va='center',
            fontsize=9, style='italic', color='#2C3E50')

ax6.set_xlim(-0.8, len(frameworks))
ax6.set_ylim(-1, max(len(fw["frameworks"]) for fw in frameworks) + 1)
ax6.set_title("Framework Evolution\nby Time Period", fontsize=14, fontweight='bold', color='#2C3E50')
ax6.set_xticks([])
ax6.set_yticks([])
ax6.set_facecolor(bg_color)

# 7. Specialization Timeline (Third Row Center)
ax7 = fig.add_subplot(gs[2, 1])

specializations = data["technology_evolution"]["specializations"]

# Create specialization flow
for i, spec in enumerate(specializations):
    year = spec["year"]
    specialization = spec["specialization"]

    # Draw specialization node
    circle = Circle((i, 0), 0.3, facecolor=colors[i % len(colors)],
                   alpha=0.8, edgecolor='white', linewidth=2)
    ax7.add_patch(circle)

    # Add specialization text
    ax7.text(i, 0.6, specialization[:15] + "..." if len(specialization) > 15 else specialization,
            ha='center', va='center', fontsize=9, fontweight='bold',
            color=colors[i % len(colors)], wrap=True)

    # Add year
    ax7.text(i, -0.6, str(year), ha='center', va='center',
            fontsize=10, fontweight='bold', color='#7F8C8D')

    # Connect to next specialization
    if i < len(specializations) - 1:
        ax7.arrow(i + 0.3, 0, 0.4, 0, head_width=0.1, head_length=0.1,
                 fc='#BDC3C7', ec='#BDC3C7', alpha=0.7)

ax7.set_xlim(-0.5, len(specializations))
ax7.set_ylim(-1, 1)
ax7.set_title("Specialization\nEvolution", fontsize=14, fontweight='bold', color='#2C3E50')
ax7.set_xticks([])
ax7.set_yticks([])
ax7.set_facecolor(bg_color)

# 8. Project Productivity Over Time (Third Row Right)
ax8 = fig.add_subplot(gs[2, 2])

# Calculate projects per year
year_counts = df["year"].value_counts().sort_index()
productivity_years = year_counts.index.tolist()
productivity_counts = year_counts.values.tolist()

# Create bar chart with trend line
bars = ax8.bar(productivity_years, productivity_counts,
               color=[colors[i % len(colors)] for i in range(len(productivity_years))],
               alpha=0.8, edgecolor='white', linewidth=2)

# Add trend line (if there are enough points)
if len(productivity_years) > 2:
    z = np.polyfit(productivity_years, productivity_counts, 1)
    p = np.poly1d(z)
    ax8.plot(productivity_years, p(productivity_years), color=primary_color,
            linestyle='--', linewidth=2, alpha=0.8, label='Trend')
    ax8.legend(loc='upper left', fontsize=10)

# Add value labels
for year, count in zip(productivity_years, productivity_counts):
    ax8.text(year, count + 0.1, str(count), ha='center', va='bottom',
            fontsize=11, fontweight='bold', color='#2C3E50')

ax8.set_title("Project Productivity\nby Year", fontsize=14, fontweight='bold', color='#2C3E50')
ax8.set_xlabel("Year", fontsize=12, fontweight='bold')
ax8.set_ylabel("Projects Created", fontsize=12, fontweight='bold')
ax8.grid(True, alpha=0.3, axis='y')
ax8.set_facecolor(bg_color)

# 9. Comprehensive Timeline Summary (Fourth Row - Full Width)
ax9 = fig.add_subplot(gs[3, :])

# Create comprehensive project timeline
timeline_y = 0
all_years = sorted(df["year"].unique())

for year in all_years:
    year_projects = df[df["year"] == year]

    # Draw year marker
    ax9.scatter(year, timeline_y, s=len(year_projects) * 100,
               color=colors[(year - 2016) % len(colors)],
               alpha=0.8, edgecolor='white', linewidth=3, zorder=10)

    # Add project count
    ax9.text(year, timeline_y + 0.15, str(len(year_projects)),
            ha='center', va='center', fontsize=12, fontweight='bold',
            color='white')

    # Add year projects summary
    project_names = [proj["name"][:15] + "..." if len(proj["name"]) > 15 else proj["name"]
                    for _, proj in year_projects.iterrows()]
    summary_text = "\n".join(project_names[:3])  # Show max 3 projects
    if len(year_projects) > 3:
        summary_text += f"\n+ {len(year_projects) - 3} more..."

    y_offset = 0.4 if (year - 2016) % 2 == 0 else -0.4
    ax9.annotate(summary_text,
                xy=(year, timeline_y),
                xytext=(year, y_offset),
                ha='center', va='center',
                fontsize=9, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.4",
                         facecolor=colors[(year - 2016) % len(colors)],
                         alpha=0.9, edgecolor='white', linewidth=2),
                arrowprops=dict(arrowstyle='->',
                               color=colors[(year - 2016) % len(colors)], lw=2),
                color='white')

# Draw main timeline
ax9.plot([2015.5, 2025.5], [timeline_y, timeline_y],
         color='#34495E', linewidth=6, alpha=0.8, zorder=5)

# Add development phases as background
for start, end, phase, color, label in phases:
    if start != end:
        ax9.axvspan(start - 0.4, end + 0.4, alpha=0.1, color=color, zorder=1)

ax9.set_xlim(2015.5, 2025.5)
ax9.set_ylim(-0.8, 0.8)
ax9.set_xlabel("Year", fontsize=14, fontweight='bold')
ax9.set_title("Complete Project Timeline Overview: All Personal Projects & Innovations",
             fontsize=16, fontweight='bold', color='#2C3E50')
ax9.set_yticks([])
ax9.spines['left'].set_visible(False)
ax9.spines['right'].set_visible(False)
ax9.spines['top'].set_visible(False)
ax9.grid(True, alpha=0.3, axis='x')
ax9.set_facecolor(bg_color)

# Overall styling and title
fig.suptitle("Personal Project Innovation Timeline: Technology Evolution & Creative Excellence\nComprehensive Analysis of Open Source Development Journey (2016-2025)",
            fontsize=22, fontweight='bold', color='#2C3E50', y=0.98)

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Projectwise Personal Highlights",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

plt.tight_layout()

# Save the timeline
output_path = "../visual/projectwise_innovation_timeline.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print(f"Projectwise innovation timeline saved to: {output_path}")