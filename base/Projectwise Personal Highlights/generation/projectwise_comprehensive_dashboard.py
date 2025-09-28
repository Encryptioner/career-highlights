import matplotlib.pyplot as plt
import pandas as pd
import json
import numpy as np
from math import pi
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch
import matplotlib.gridspec as gridspec

# Set style
plt.style.use('default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

# Load the project data
file_path = "../graphical/diagram_ready_data.json"
with open(file_path, "r") as f:
    data = json.load(f)

# Create the comprehensive project dashboard
fig = plt.figure(figsize=(24, 16))

# Create complex grid layout
gs_main = gridspec.GridSpec(4, 4, figure=fig, hspace=0.4, wspace=0.3,
                           height_ratios=[1, 0.8, 0.8, 0.6], width_ratios=[1, 1, 1, 1], top=0.88)

# Define color scheme
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FCEA2B', '#FF9F43', '#A29BFE', '#6C5CE7', '#FD79A8', '#00CEC9']
bg_color = '#FAFAFA'
primary_color = '#FF6B6B'
secondary_color = '#4ECDC4'

# 1. Project Timeline Evolution (Top Section - Full Width)
ax_main = fig.add_subplot(gs_main[0, :])

projects_timeline = data["projects_timeline"]
df = pd.DataFrame(projects_timeline)

# Create gradient background
gradient = np.linspace(0, 1, 256).reshape(1, -1)
ax_main.imshow(gradient, extent=[2015.5, 2025.5, 0, 6], aspect='auto', cmap='plasma', alpha=0.05)

# Plot projects by complexity with year grouping
years = df["year"].unique()
year_project_counts = df.groupby('year').size()
year_complexity_avg = df.groupby('year')['complexity'].mean()

# Create bars for project counts
bars = ax_main.bar(years, year_project_counts,
                   color=[colors[i % len(colors)] for i in range(len(years))],
                   alpha=0.8, edgecolor='white', linewidth=2, width=0.6)

# Add complexity line on secondary axis
ax_main_twin = ax_main.twinx()
complexity_line = ax_main_twin.plot(years, year_complexity_avg, color=primary_color,
                                   marker='D', linewidth=4, markersize=10,
                                   markerfacecolor='white', markeredgecolor=primary_color,
                                   markeredgewidth=3, label="Average Complexity", zorder=10)

# Add project count labels
for year, count in year_project_counts.items():
    ax_main.text(year, count + 0.1, str(count),
                ha="center", va="bottom", fontsize=11, fontweight='bold', color='#2C3E50')

# Add development phase annotations
phases = [(2016, 2018, 'Foundation', secondary_color),
          (2019, 2019, 'Real-time', '#F39C12'),
          (2022, 2022, 'Enterprise', '#9B59B6'),
          (2024, 2025, 'Innovation Boom', primary_color)]

for start, end, phase, color in phases:
    if start == end:
        ax_main.axvline(x=start, color=color, alpha=0.3, linewidth=3)
        ax_main.text(start, 5.5, phase, ha='center', va='center',
                    fontsize=11, fontweight='bold', color=color,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9,
                             edgecolor=color, linewidth=2))
    else:
        ax_main.axvspan(start - 0.4, end + 0.4, alpha=0.1, color=color)
        ax_main.text((start + end) / 2, 5.5, phase, ha='center', va='center',
                    fontsize=11, fontweight='bold', color=color,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9,
                             edgecolor=color, linewidth=2))

# Styling
ax_main.set_xlabel("Year", fontsize=14, fontweight='bold')
ax_main.set_ylabel("Number of Projects", fontsize=14, fontweight='bold')
ax_main_twin.set_ylabel("Average Complexity Level", fontsize=14, fontweight='bold', color=primary_color)
ax_main.grid(True, alpha=0.3)
ax_main.set_facecolor(bg_color)
ax_main.set_xlim(2015.5, 2025.5)
ax_main.set_ylim(0, 6)
ax_main_twin.set_ylim(0, 6)

# 2. Project Categories Distribution (Top Left of Second Row)
ax_categories = fig.add_subplot(gs_main[1, 0])

project_categories = data["project_categories"]
categories = list(project_categories.keys())
counts = [project_categories[cat]["count"] for cat in categories]
cat_colors = colors[:len(categories)]

# Create donut chart
wedges, texts, autotexts = ax_categories.pie(counts, labels=None,
                                           colors=cat_colors, autopct='%1.0f',
                                           startangle=90, textprops={'fontsize': 10, 'fontweight': 'bold'},
                                           pctdistance=0.85, wedgeprops=dict(width=0.6))

# Add center circle with total
centre_circle = Circle((0,0), 0.4, fc='white', linewidth=2, edgecolor='#2C3E50')
ax_categories.add_artist(centre_circle)
ax_categories.text(0, 0, f'{sum(counts)}\nProjects', ha='center', va='center',
                  fontsize=14, fontweight='bold', color='#2C3E50')

ax_categories.set_title("Project Categories\nDistribution", fontsize=14, fontweight='bold', color='#2C3E50')

# Create legend with shortened names
legend_labels = [cat.replace('_', ' ').replace(' ', '\n') for cat in categories]
ax_categories.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9)

# 3. Technology Evolution Flow (Top Center)
ax_tech_flow = fig.add_subplot(gs_main[1, 1])

tech_evolution = data["technology_evolution"]["languages"]

# Create technology progression visualization
for i, tech_year in enumerate(tech_evolution):
    year = tech_year["year"]
    primary = tech_year["primary"]
    focus = tech_year["focus"]

    # Draw year marker
    ax_tech_flow.scatter(i, 0, s=200, color=colors[i % len(colors)],
                        alpha=0.8, edgecolor='white', linewidth=2, zorder=10)

    # Add primary technology
    ax_tech_flow.text(i, 0.3, primary, ha='center', va='bottom',
                     fontsize=10, fontweight='bold', color=colors[i % len(colors)])

    # Add focus area
    ax_tech_flow.text(i, -0.3, focus[:15] + "..." if len(focus) > 15 else focus,
                     ha='center', va='top', fontsize=8, style='italic',
                     color='#2C3E50', wrap=True)

    # Add year label
    ax_tech_flow.text(i, -0.6, str(year), ha='center', va='center',
                     fontsize=9, fontweight='bold', color='#7F8C8D')

    # Draw connection line to next technology
    if i < len(tech_evolution) - 1:
        ax_tech_flow.plot([i + 0.1, i + 0.9], [0, 0], color='#BDC3C7',
                         linewidth=2, alpha=0.7, zorder=5)

ax_tech_flow.set_xlim(-0.5, len(tech_evolution))
ax_tech_flow.set_ylim(-0.8, 0.8)
ax_tech_flow.set_title("Technology Evolution\nTimeline", fontsize=14, fontweight='bold', color='#2C3E50')
ax_tech_flow.set_xticks([])
ax_tech_flow.set_yticks([])
ax_tech_flow.set_facecolor(bg_color)

# 4. Complexity by Year Analysis (Top Center-Right)
ax_complexity = fig.add_subplot(gs_main[1, 2])

complexity_by_year = data["complexity_by_year"]
years_complex = list(complexity_by_year.keys())
averages = [complexity_by_year[year]["average"] for year in years_complex]
peaks = [complexity_by_year[year]["peak"] for year in years_complex]
project_counts = [complexity_by_year[year]["projects"] for year in years_complex]

# Convert years to integers for plotting
years_int = [int(year) for year in years_complex]

# Create bubble chart
bubbles = ax_complexity.scatter(years_int, averages, s=[count*50 for count in project_counts],
                               c=colors[:len(years_int)], alpha=0.7,
                               edgecolors='white', linewidths=2)

# Add peak complexity line
ax_complexity.plot(years_int, peaks, color=primary_color, linestyle='--',
                  linewidth=2, alpha=0.8, label='Peak Complexity')

# Add labels
for i, (year, avg, peak, count) in enumerate(zip(years_int, averages, peaks, project_counts)):
    ax_complexity.text(year, avg, str(count), ha='center', va='center',
                      fontsize=10, fontweight='bold', color='white')

ax_complexity.set_title("Complexity Evolution\n(Bubble Size = Project Count)",
                       fontsize=14, fontweight='bold', color='#2C3E50')
ax_complexity.set_xlabel("Year", fontsize=12, fontweight='bold')
ax_complexity.set_ylabel("Complexity Level", fontsize=12, fontweight='bold')
ax_complexity.grid(True, alpha=0.3)
ax_complexity.set_facecolor(bg_color)
ax_complexity.legend(loc='upper left', fontsize=10)

# 5. Open Source Impact (Top Right)
ax_opensource = fig.add_subplot(gs_main[1, 3])

os_impact = data["open_source_impact"]
community_contributions = os_impact["community_contributions"]

# Create horizontal bar chart
categories_os = list(community_contributions.keys())
values_os = list(community_contributions.values())

bars = ax_opensource.barh(range(len(categories_os)), values_os,
                         color=colors[:len(categories_os)], alpha=0.8,
                         edgecolor='white', linewidth=2)

# Add value labels
for i, (bar, value) in enumerate(zip(bars, values_os)):
    ax_opensource.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                      str(value), va='center', fontsize=11, fontweight='bold')

ax_opensource.set_yticks(range(len(categories_os)))
readable_labels = [cat.replace('_', ' ').title() for cat in categories_os]
ax_opensource.set_yticklabels(readable_labels, fontsize=10)
ax_opensource.set_title(f"Open Source Impact\n({os_impact['total_projects']} Projects - 100% Open)",
                       fontsize=14, fontweight='bold', color='#2C3E50')
ax_opensource.set_xlabel("Project Count", fontsize=12, fontweight='bold')
ax_opensource.grid(True, alpha=0.3, axis='x')
ax_opensource.set_facecolor(bg_color)

# 6. Deployment Evolution (Second Row Left)
ax_deployment = fig.add_subplot(gs_main[2, 0])

deployment_evolution = data["deployment_evolution"]
deploy_periods = list(deployment_evolution.keys())
deploy_projects = [deployment_evolution[period]["projects"] for period in deploy_periods]
deploy_methods = [deployment_evolution[period]["method"] for period in deploy_periods]

# Create timeline visualization
for i, (period, projects, method) in enumerate(zip(deploy_periods, deploy_projects, deploy_methods)):
    # Draw period rectangle
    width = projects * 0.3  # Scale width by number of projects
    rect = FancyBboxPatch((i - width/2, 0), width, 0.8,
                         boxstyle="round,pad=0.05",
                         facecolor=colors[i % len(colors)], alpha=0.8,
                         edgecolor='white', linewidth=2)
    ax_deployment.add_patch(rect)

    # Add method text
    ax_deployment.text(i, 0.4, method.replace(' ', '\n'), ha='center', va='center',
                      fontsize=9, fontweight='bold', color='white')

    # Add project count
    ax_deployment.text(i, -0.3, f'{projects} projects', ha='center', va='center',
                      fontsize=10, fontweight='bold', color=colors[i % len(colors)])

    # Add period label
    ax_deployment.text(i, -0.6, period, ha='center', va='center',
                      fontsize=9, style='italic', color='#7F8C8D')

ax_deployment.set_xlim(-0.8, len(deploy_periods))
ax_deployment.set_ylim(-0.8, 1.2)
ax_deployment.set_title("Deployment Evolution\nAcross Time Periods", fontsize=14, fontweight='bold', color='#2C3E50')
ax_deployment.set_xticks([])
ax_deployment.set_yticks([])
ax_deployment.set_facecolor(bg_color)

# 7. Architecture Patterns Timeline (Second Row Center)
ax_architecture = fig.add_subplot(gs_main[2, 1])

arch_patterns = data["technical_architecture_patterns"]
patterns = list(arch_patterns.keys())
pattern_projects = [arch_patterns[pattern]["projects"] for pattern in patterns]
pattern_periods = [arch_patterns[pattern]["period"] for pattern in patterns]

# Create stacked timeline
y_offset = 0
for i, (pattern, projects, period) in enumerate(zip(patterns, pattern_projects, pattern_periods)):
    # Draw pattern block
    rect = Rectangle((0, y_offset), projects, 0.8,
                    facecolor=colors[i % len(colors)], alpha=0.8,
                    edgecolor='white', linewidth=2)
    ax_architecture.add_patch(rect)

    # Add pattern label
    pattern_name = pattern.replace('_', ' ')
    ax_architecture.text(projects/2, y_offset + 0.4, f'{pattern_name}\n({period})',
                        ha='center', va='center', fontsize=9, fontweight='bold',
                        color='white')

    # Add project count
    ax_architecture.text(projects + 0.2, y_offset + 0.4, str(projects),
                        ha='left', va='center', fontsize=11, fontweight='bold',
                        color=colors[i % len(colors)])

    y_offset += 1

ax_architecture.set_xlim(0, max(pattern_projects) + 1)
ax_architecture.set_ylim(0, len(patterns))
ax_architecture.set_title("Architecture Pattern\nEvolution", fontsize=14, fontweight='bold', color='#2C3E50')
ax_architecture.set_xlabel("Project Count", fontsize=12, fontweight='bold')
ax_architecture.set_yticks([])
ax_architecture.grid(True, alpha=0.3, axis='x')
ax_architecture.set_facecolor(bg_color)

# 8. Cross-Project Reusability (Second Row Center-Right)
ax_reusability = fig.add_subplot(gs_main[2, 2])

reusability_data = data["cross_project_reusability"]
reuse_categories = list(reusability_data.keys())
reuse_counts = [reusability_data[cat]["projects"] for cat in reuse_categories]

# Create polar bar chart
angles = np.linspace(0, 2*pi, len(reuse_categories), endpoint=False)
ax_reusability = plt.subplot(gs_main[2, 2], projection='polar')

bars = ax_reusability.bar(angles, reuse_counts, width=0.8, alpha=0.8,
                         color=colors[:len(reuse_categories)],
                         edgecolor='white', linewidth=2)

ax_reusability.set_xticks(angles)
readable_reuse = [cat.replace('_', '\n').replace(' ', '\n') for cat in reuse_categories]
ax_reusability.set_xticklabels(readable_reuse, fontsize=9, fontweight='bold')
ax_reusability.set_title("Cross-Project\nReusability", fontsize=14, fontweight='bold',
                        color='#2C3E50', pad=25)
ax_reusability.grid(True, alpha=0.3)

# 9. User Experience Evolution (Second Row Right)
ax_ux = fig.add_subplot(gs_main[2, 3])

ux_evolution = data["user_experience_evolution"]
ux_phases = list(ux_evolution.keys())
ux_projects = [ux_evolution[phase]["projects"] for phase in ux_phases]
ux_priorities = [ux_evolution[phase]["priority"] for phase in ux_phases]

# Create area chart
x_pos = range(len(ux_phases))
ax_ux.fill_between(x_pos, ux_projects, alpha=0.4, color=secondary_color)
ax_ux.plot(x_pos, ux_projects, color=secondary_color, linewidth=3,
           marker='o', markersize=8, markerfacecolor='white',
           markeredgecolor=secondary_color, markeredgewidth=2)

# Add priority annotations
for i, (phase, projects, priority) in enumerate(zip(ux_phases, ux_projects, ux_priorities)):
    ax_ux.annotate(priority[:15] + "..." if len(priority) > 15 else priority,
                   xy=(i, projects), xytext=(i, projects + 1),
                   ha='center', fontsize=9, fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor=secondary_color, alpha=0.7),
                   color='white')

ax_ux.set_xticks(x_pos)
ux_labels = [phase.replace('_', ' ') for phase in ux_phases]
ax_ux.set_xticklabels(ux_labels, rotation=45, ha='right', fontsize=9)
ax_ux.set_title("UX Evolution\nFocus Areas", fontsize=14, fontweight='bold', color='#2C3E50')
ax_ux.set_ylabel("Projects", fontsize=12, fontweight='bold')
ax_ux.grid(True, alpha=0.3)
ax_ux.set_facecolor(bg_color)

# 10. Innovation Milestones Timeline (Bottom Section - Full Width)
ax_innovation = fig.add_subplot(gs_main[3, :])

innovation_milestones = data["innovation_milestones"]
milestone_df = pd.DataFrame(innovation_milestones)

# Create timeline
timeline_y = 0
for i, (_, row) in enumerate(milestone_df.iterrows()):
    color = colors[i % len(colors)]

    # Draw milestone point
    ax_innovation.scatter(row["year"], timeline_y, s=400, color=color,
                         alpha=0.9, edgecolor='white', linewidth=3, zorder=10)

    # Add milestone text with alternating positions
    y_offset = 0.4 if i % 2 == 0 else -0.4
    ax_innovation.annotate(f'{row["milestone"]}\n({row["impact"]})',
                          xy=(row["year"], timeline_y),
                          xytext=(row["year"], y_offset),
                          ha='center', va='center',
                          fontsize=10, fontweight='bold',
                          bbox=dict(boxstyle="round,pad=0.4", facecolor=color,
                                   alpha=0.9, edgecolor='white', linewidth=2),
                          arrowprops=dict(arrowstyle='->', color=color, lw=2),
                          color='white')

# Draw main timeline
ax_innovation.plot([2015.5, 2025.5], [timeline_y, timeline_y],
                  color='#34495E', linewidth=6, alpha=0.8, zorder=5)

# Add year markers
for year in range(2016, 2026):
    if year in [2016, 2017, 2018, 2019, 2022, 2024, 2025]:  # Years with projects
        ax_innovation.axvline(x=year, color=primary_color, linestyle='--', alpha=0.3, zorder=1)

ax_innovation.set_xlim(2015.5, 2025.5)
ax_innovation.set_ylim(-0.8, 0.8)
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
fig.suptitle("Personal Project Portfolio: Innovation Journey & Technical Excellence Dashboard\nOpen Source Development & Cutting-Edge Technology Exploration (2016-2025)",
            fontsize=24, fontweight='bold', color='#2C3E50', y=0.94)

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Projectwise Personal Highlights",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

plt.tight_layout()
plt.subplots_adjust(top=0.88)

# Save the comprehensive dashboard
output_path = "../visual/projectwise_comprehensive_dashboard.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print(f"Projectwise comprehensive dashboard saved to: {output_path}")