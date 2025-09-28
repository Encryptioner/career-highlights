#!/usr/bin/env python3
"""
Nerddevs Projectwise Technology Evolution Analysis
Professional Technology Stack Progression & Innovation Timeline (2019-2025)

This script creates specialized visualizations focusing on technology adoption,
stack evolution, and innovation patterns across professional projects.
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import json
import seaborn as sns
from math import pi
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)

# Load data using relative path
data_path = os.path.join(project_dir, 'graphical', 'diagram_ready_data.json')
with open(data_path, 'r') as f:
    data = json.load(f)

# Set style and colors
plt.style.use('default')
config = data['visualization_config']
colors = config['color_schemes']
sns.set_palette(colors['primary_colors'])

# Create the technology evolution dashboard
fig = plt.figure(figsize=(20, 16))
fig.patch.set_facecolor('#F8F9FA')

# Create grid layout
gs_main = gridspec.GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.3,
                           height_ratios=[1.2, 1, 1], width_ratios=[1, 1, 1])

# Main title
fig.suptitle('⚡ Nerddevs Professional Technology Evolution: Innovation & Stack Mastery\n'
            'Comprehensive Technology Adoption & Growth Analysis (2019-2025)',
            fontsize=18, fontweight='bold', y=0.96, color='#2C3E50')

# 1. Technology Stack Timeline (Top - Full Width)
ax1 = fig.add_subplot(gs_main[0, :])
tech_data = data['technology_stack_usage']

# Prepare timeline data
years = list(range(2019, 2026))
tech_categories = ['Frontend', 'Backend', 'Databases', 'Mobile', 'AI_ML']
all_techs = []
tech_years = []
tech_categories_list = []
tech_project_counts = []

for category, techs in tech_data.items():
    for tech_name, info in techs.items():
        all_techs.append(tech_name)
        tech_years.append(info['years'])
        tech_categories_list.append(category)
        tech_project_counts.append(info['projects'])

# Create technology adoption timeline
y_pos = 0
category_positions = {}
for category_idx, category in enumerate(tech_categories):
    category_positions[category] = y_pos
    category_techs = [(tech, years_list, projects) for tech, years_list, cat, projects
                     in zip(all_techs, tech_years, tech_categories_list, tech_project_counts)
                     if cat == category]

    for i, (tech, years_list, projects) in enumerate(category_techs):
        color = colors['category_colors'].get(category, colors['primary_colors'][category_idx % len(colors['primary_colors'])])

        # Draw timeline for each technology
        y_position = y_pos + i * 0.8
        if years_list:
            start_year = min(years_list)
            end_year = max(years_list)
            duration = end_year - start_year + 1

            # Draw technology bar
            alpha_value = min(0.7 + (projects * 0.02), 1.0)  # Cap alpha at 1.0
            ax1.barh(y_position, duration, left=start_year, height=0.6,
                    color=color, alpha=alpha_value, edgecolor='white', linewidth=2)

            # Add technology name and project count
            ax1.text(start_year + duration/2, y_position, f'{tech}\n({projects} projects)',
                    ha='center', va='center', fontsize=8, fontweight='bold', color='white')

    # Add category separator
    ax1.axhline(y=y_pos + len(category_techs) * 0.8, color='gray', linestyle='--', alpha=0.5)
    y_pos += len(category_techs) * 0.8 + 1

ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_title('🚀 Technology Adoption Timeline: Professional Stack Evolution', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlim(2018.5, 2025.5)
ax1.grid(True, alpha=0.3, axis='x')

# Add category labels
for category, pos in category_positions.items():
    ax1.text(2018.2, pos + 1, category, fontsize=10, fontweight='bold',
            rotation=90, va='center', ha='right', color='#34495E')

# Add gradient background
gradient = np.linspace(0, 1, 256).reshape(256, -1)
gradient = np.vstack((gradient, gradient))
ax1.imshow(gradient, extent=[2018.5, 2025.5, -1, y_pos], aspect='auto', cmap='viridis', alpha=0.1)

# 2. Technology Category Distribution (Middle Left)
ax2 = fig.add_subplot(gs_main[1, 0])

# Calculate project counts by technology category
category_totals = {}
for category, techs in tech_data.items():
    total_projects = sum(info['projects'] for info in techs.values())
    category_totals[category] = total_projects

categories = list(category_totals.keys())
totals = list(category_totals.values())
category_colors = [colors['category_colors'].get(cat, colors['primary_colors'][i])
                  for i, cat in enumerate(categories)]

# Create radar chart
N = len(categories)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
totals += totals[:1]

ax2 = plt.subplot(gs_main[1, 0], projection='polar')
ax2.plot(angles, totals, 'o-', linewidth=3, color='#E74C3C', markersize=8)
ax2.fill(angles, totals, alpha=0.25, color='#E74C3C')
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(categories, fontsize=10)
ax2.set_title('📊 Technology Category Distribution\nProfessional Project Usage', fontsize=12, fontweight='bold', pad=30)
ax2.grid(True, alpha=0.3)

# 3. Innovation Milestones (Middle Center)
ax3 = fig.add_subplot(gs_main[1, 1])

# Extract AI/ML projects for innovation analysis
ai_projects = []
ai_years = []
ai_complexities = []

for project in data['projects_timeline']:
    if project['category'] == 'AI':
        ai_projects.append(project['name'][:12])  # Truncate for display
        ai_years.append(project['start'])
        ai_complexities.append(project['complexity'])

# Create innovation timeline
colors_innovation = colors['complexity_gradient']
for i, (project, year, complexity) in enumerate(zip(ai_projects, ai_years, ai_complexities)):
    color_idx = min(complexity - 1, len(colors_innovation) - 1)
    ax3.scatter(year, complexity, s=complexity * 100, alpha=0.8,
               c=colors_innovation[color_idx], edgecolors='white', linewidth=2)
    ax3.annotate(project, (year, complexity), xytext=(5, 5),
                textcoords='offset points', fontsize=9, fontweight='bold')

ax3.set_xlabel('Year', fontsize=12, fontweight='bold')
ax3.set_ylabel('Project Complexity', fontsize=12, fontweight='bold')
ax3.set_title('💡 AI Innovation Milestones\nComplexity Evolution', fontsize=12, fontweight='bold', pad=20)
ax3.grid(True, alpha=0.3)
ax3.set_ylim(0, 6)

# 4. Technology Stack Heatmap (Middle Right)
ax4 = fig.add_subplot(gs_main[1, 2])

# Create heatmap data
heatmap_data = []
tech_names = []
for category, techs in tech_data.items():
    for tech_name, info in techs.items():
        tech_row = [1 if year in info['years'] else 0 for year in years]
        heatmap_data.append(tech_row)
        tech_names.append(f"{tech_name}")

# Create heatmap
heatmap_array = np.array(heatmap_data)
im = ax4.imshow(heatmap_array, cmap='RdYlBu_r', aspect='auto', alpha=0.8)

ax4.set_xticks(range(len(years)))
ax4.set_xticklabels(years)
ax4.set_yticks(range(len(tech_names)))
ax4.set_yticklabels(tech_names, fontsize=8)
ax4.set_xlabel('Year', fontsize=12, fontweight='bold')
ax4.set_title('🔥 Technology Usage Heatmap\nTech Stack Timeline', fontsize=12, fontweight='bold', pad=20)

# Add colorbar
cbar = plt.colorbar(im, ax=ax4, shrink=0.8)
cbar.set_label('Technology Active', fontsize=10)

# 5. DevOps Evolution (Bottom Left)
ax5 = fig.add_subplot(gs_main[2, 0])
devops_data = data['development_methodology_evolution']['DevOps_Evolution']

devops_years = [entry['period'] for entry in devops_data]
devops_levels = [entry['level'] for entry in devops_data]
project_counts = [entry['projects'] for entry in devops_data]

# Create evolution chart
x_positions = range(len(devops_years))
bars = ax5.bar(x_positions, project_counts, color=colors['primary_colors'][:len(devops_years)],
               alpha=0.8, edgecolor='white', linewidth=2)

# Add level labels
for i, (bar, level, count) in enumerate(zip(bars, devops_levels, project_counts)):
    ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'{level}\n({count})', ha='center', va='bottom',
            fontsize=9, fontweight='bold')

ax5.set_xticks(x_positions)
ax5.set_xticklabels(devops_years, rotation=45, ha='right')
ax5.set_ylabel('Projects Using Level', fontsize=12, fontweight='bold')
ax5.set_title('🛠️ DevOps Evolution\nProfessional Methodology', fontsize=12, fontweight='bold', pad=20)
ax5.grid(True, alpha=0.3, axis='y')

# 6. Technology Adoption Flow (Bottom Center)
ax6 = fig.add_subplot(gs_main[2, 1])

# Calculate technology adoption by year
adoption_by_year = {}
for year in years:
    adoption_count = 0
    for category, techs in tech_data.items():
        for tech_name, info in techs.items():
            if year in info['years']:
                adoption_count += 1
    adoption_by_year[year] = adoption_count

# Create flow chart
years_list = list(adoption_by_year.keys())
counts = list(adoption_by_year.values())

ax6.plot(years_list, counts, marker='o', linewidth=3, markersize=8,
         color='#3498DB', markerfacecolor='#E74C3C', markeredgecolor='white', markeredgewidth=2)
ax6.fill_between(years_list, counts, alpha=0.3, color='#3498DB')

ax6.set_xlabel('Year', fontsize=12, fontweight='bold')
ax6.set_ylabel('Active Technologies', fontsize=12, fontweight='bold')
ax6.set_title('📈 Technology Adoption Flow\nStack Growth Pattern', fontsize=12, fontweight='bold', pad=20)
ax6.grid(True, alpha=0.3)

# 7. Technology Complexity Analysis (Bottom Right)
ax7 = fig.add_subplot(gs_main[2, 2])

# Analyze complexity by technology category
complexity_data = {}
for category, techs in tech_data.items():
    total_projects = sum(info['projects'] for info in techs.values())
    avg_complexity = total_projects / len(techs) if techs else 0
    complexity_data[category] = {'total': total_projects, 'avg': avg_complexity}

categories = list(complexity_data.keys())
totals = [complexity_data[cat]['total'] for cat in categories]
averages = [complexity_data[cat]['avg'] for cat in categories]

# Create scatter plot
for i, (cat, total, avg) in enumerate(zip(categories, totals, averages)):
    color = colors['category_colors'].get(cat, colors['primary_colors'][i])
    ax7.scatter(total, avg, s=avg * 30, alpha=0.8, c=color, edgecolors='white', linewidth=2)
    ax7.annotate(cat, (total, avg), xytext=(5, 5), textcoords='offset points',
                fontsize=10, fontweight='bold')

ax7.set_xlabel('Total Projects', fontsize=12, fontweight='bold')
ax7.set_ylabel('Average Project/Tech Ratio', fontsize=12, fontweight='bold')
ax7.set_title('⚡ Technology Impact Analysis\nCategory Effectiveness', fontsize=12, fontweight='bold', pad=20)
ax7.grid(True, alpha=0.3)

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Projectwise Highlights in ND",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

# Ensure output directory exists
output_dir = os.path.join(project_dir, 'visual')
os.makedirs(output_dir, exist_ok=True)

# Save the visualization using relative path (will override existing file)
output_path = os.path.join(output_dir, 'projectwise_nd_technology_evolution.png')
plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#F8F9FA', edgecolor='none')

print("✅ Nerddevs Projectwise Technology Evolution Analysis generated successfully!")
print(f"📁 Saved to: {output_path}")
print("⚡ Analysis includes: Technology Timeline, Category Distribution, Innovation Milestones, Usage Heatmap, DevOps Evolution, Adoption Flow & Impact Analysis")