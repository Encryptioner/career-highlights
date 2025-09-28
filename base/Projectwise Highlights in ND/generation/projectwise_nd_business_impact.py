#!/usr/bin/env python3
"""
Nerddevs Projectwise Business Impact & Scale Analysis
Professional Project Portfolio: User Impact, Business Value & Market Reach (2019-2025)

This script creates visualizations focusing on business impact, user scale,
and market penetration of professional projects across different industries.
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import json
import seaborn as sns
from matplotlib.patches import Circle
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

# Create the business impact dashboard
fig = plt.figure(figsize=(20, 16))
fig.patch.set_facecolor('#F8F9FA')

# Create grid layout
gs_main = gridspec.GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.3,
                           height_ratios=[1, 1, 0.8], width_ratios=[1.2, 1, 1])

# Main title
fig.suptitle('Nerddevs Professional Business Impact: Scale, Value & Market Reach',
            fontsize=18, fontweight='bold', y=0.96, color='#2C3E50')

# 1. User Scale Impact Analysis (Top Left - Large)
ax1 = fig.add_subplot(gs_main[0, :2])
user_scale_data = data['user_scale_by_project']
projects = data['projects_timeline']
project_complexities = {p['name']: p['complexity'] for p in projects}

# Prepare bubble chart data
project_names = []
user_impacts = []
complexities = []
categories = []
years = []

for project in projects:
    project_name = project['name']
    if project_name in user_scale_data:
        scale_info = user_scale_data[project_name]
        project_names.append(project_name[:15])  # Truncate for display

        # Extract user impact
        user_impact = 0
        if 'peak_users' in scale_info:
            user_impact = scale_info['peak_users']
        elif 'monthly_active' in scale_info:
            user_impact = scale_info['monthly_active']
        elif 'active_users' in scale_info:
            user_impact = scale_info['active_users']
        elif 'users' in scale_info:
            user_impact = scale_info['users']
        elif 'companies' in scale_info:
            user_impact = scale_info['companies'] * 100  # Scale up for visualization

        user_impacts.append(user_impact)
        complexities.append(project['complexity'])
        categories.append(project['category'])
        years.append(project['start'])

# Create enhanced bubble chart
for i, (name, impact, complexity, category, year) in enumerate(zip(project_names, user_impacts, complexities, categories, years)):
    color = colors['category_colors'].get(category, colors['primary_colors'][i % len(colors['primary_colors'])])

    # Bubble size based on impact and complexity
    bubble_size = (impact / 500) + (complexity * 50) + 100

    # Create bubble with gradient effect
    ax1.scatter(year, impact, s=bubble_size, alpha=0.7, c=color, edgecolors='white', linewidth=3)

    # Add project labels
    ax1.annotate(f'{name}\nLevel {complexity}', (year, impact), xytext=(5, 5),
                textcoords='offset points', fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

ax1.set_xlabel('Project Start Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('User Impact Scale (Log Scale)', fontsize=12, fontweight='bold')
ax1.set_title('🚀 Professional Projects: User Impact vs Timeline Analysis\nBubble size represents complexity + user scale', fontsize=14, fontweight='bold', pad=20)
ax1.set_yscale('log')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(2018.5, 2025.5)

# Add gradient background
gradient = np.linspace(0, 1, 256).reshape(256, -1)
gradient = np.vstack((gradient, gradient))
ax1.imshow(gradient, extent=[2018.5, 2025.5, min(user_impacts)*0.1, max(user_impacts)*1.5],
          aspect='auto', cmap='Blues', alpha=0.1)

# 2. Business Domain Distribution (Top Right)
ax2 = fig.add_subplot(gs_main[0, 2])
domain_data = data['business_domain_distribution']

domains = list(domain_data.keys())
project_counts = [domain_data[domain]['projects'] for domain in domains]
domain_colors = [colors['primary_colors'][i % len(colors['primary_colors'])] for i in range(len(domains))]

# Create enhanced donut chart
wedges, texts, autotexts = ax2.pie(project_counts, labels=[d.replace('_', '\n') for d in domains],
                                   autopct='%1.0f', startangle=90, colors=domain_colors,
                                   pctdistance=0.85, explode=[0.05] * len(domains))

# Create center circle for donut effect
centre_circle = Circle((0,0), 0.70, fc='white')
ax2.add_artist(centre_circle)

# Enhance text appearance
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

for text in texts:
    text.set_fontsize(8)
    text.set_fontweight('bold')

ax2.set_title('🏢 Business Domain Distribution\nProfessional Portfolio Spread', fontsize=12, fontweight='bold', pad=20)

# Add center text
ax2.text(0, 0, f'Total\n{sum(project_counts)}\nProjects', ha='center', va='center',
         fontsize=14, fontweight='bold', color='#2C3E50')

# 3. Category vs Complexity Analysis (Middle Left)
ax3 = fig.add_subplot(gs_main[1, 0])
categories_data = data['project_categories']

category_names = list(categories_data.keys())
avg_complexities = [categories_data[cat]['complexity_avg'] for cat in category_names]
user_peaks = [categories_data[cat]['users_peak'] for cat in category_names]

# Create scatter plot with category analysis
for i, (cat, complexity, users) in enumerate(zip(category_names, avg_complexities, user_peaks)):
    color = colors['category_colors'].get(cat, colors['primary_colors'][i])
    size = (users / 1000) + 100  # Scale bubble size
    ax3.scatter(complexity, users, s=size, alpha=0.8, c=color, edgecolors='white', linewidth=2)
    ax3.annotate(cat, (complexity, users), xytext=(5, 5), textcoords='offset points',
                fontsize=9, fontweight='bold')

ax3.set_xlabel('Average Complexity', fontsize=12, fontweight='bold')
ax3.set_ylabel('Peak Users', fontsize=12, fontweight='bold')
ax3.set_title('📊 Category Impact Analysis\nComplexity vs User Reach', fontsize=12, fontweight='bold', pad=20)
ax3.set_yscale('log')
ax3.grid(True, alpha=0.3)

# 4. Project Status Distribution (Middle Center)
ax4 = fig.add_subplot(gs_main[1, 1])

# Calculate status distribution
status_counts = {}
for project in projects:
    status = project['status']
    status_counts[status] = status_counts.get(status, 0) + 1

statuses = list(status_counts.keys())
counts = list(status_counts.values())
status_colors = [colors['status_colors'].get(status, colors['primary_colors'][i])
                for i, status in enumerate(statuses)]

# Create bar chart
bars = ax4.bar(statuses, counts, color=status_colors, alpha=0.8, edgecolor='white', linewidth=2)

# Add count labels
for bar, count in zip(bars, counts):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            str(count), ha='center', va='bottom', fontweight='bold', fontsize=12)

ax4.set_ylabel('Number of Projects', fontsize=12, fontweight='bold')
ax4.set_title('📈 Project Status Distribution\nProfessional Portfolio Health', fontsize=12, fontweight='bold', pad=20)
ax4.grid(True, alpha=0.3, axis='y')

# 5. Technology Impact by Category (Middle Right)
ax5 = fig.add_subplot(gs_main[1, 2])
tech_data = data['technology_stack_usage']

# Calculate technology distribution across categories
tech_category_counts = {}
for category, techs in tech_data.items():
    tech_category_counts[category] = len(techs)

categories = list(tech_category_counts.keys())
tech_counts = list(tech_category_counts.values())
tech_colors = [colors['category_colors'].get(cat, colors['primary_colors'][i])
              for i, cat in enumerate(categories)]

# Create horizontal bar chart
y_positions = range(len(categories))
bars = ax5.barh(y_positions, tech_counts, color=tech_colors, alpha=0.8, edgecolor='white', linewidth=2)

# Add count labels
for bar, count in zip(bars, tech_counts):
    ax5.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
            str(count), va='center', fontweight='bold', fontsize=10)

ax5.set_yticks(y_positions)
ax5.set_yticklabels(categories, fontsize=10)
ax5.set_xlabel('Number of Technologies', fontsize=12, fontweight='bold')
ax5.set_title('⚡ Tech Stack Diversity\nby Category', fontsize=12, fontweight='bold', pad=20)
ax5.grid(True, alpha=0.3, axis='x')

# 6. Project Timeline with Business Impact (Bottom Left)
ax6 = fig.add_subplot(gs_main[2, 0])

# Create timeline showing business value progression
years_range = list(range(2019, 2026))
cumulative_projects = []
cumulative_users = []

for year in years_range:
    projects_by_year = [p for p in projects if p['start'] <= year]
    cumulative_projects.append(len(projects_by_year))

    total_users = 0
    for project in projects_by_year:
        if project['name'] in user_scale_data:
            scale_info = user_scale_data[project['name']]
            if 'peak_users' in scale_info:
                total_users += scale_info['peak_users']
            elif 'monthly_active' in scale_info:
                total_users += scale_info['monthly_active']

    cumulative_users.append(total_users)

# Create dual axis chart
ax6_twin = ax6.twinx()

# Plot project count
line1 = ax6.plot(years_range, cumulative_projects, marker='o', linewidth=3, color='#3498DB',
                markersize=8, label='Projects Count')
ax6.fill_between(years_range, cumulative_projects, alpha=0.3, color='#3498DB')

# Plot user impact
line2 = ax6_twin.plot(years_range, cumulative_users, marker='s', linewidth=3, color='#E74C3C',
                     markersize=8, label='Cumulative Users')

ax6.set_xlabel('Year', fontsize=12, fontweight='bold')
ax6.set_ylabel('Cumulative Projects', fontsize=12, fontweight='bold', color='#3498DB')
ax6_twin.set_ylabel('Cumulative Users', fontsize=12, fontweight='bold', color='#E74C3C')
ax6.set_title('📈 Business Growth Timeline\nProjects & User Impact', fontsize=12, fontweight='bold', pad=20)
ax6.grid(True, alpha=0.3)

# Combine legends
lines1, labels1 = ax6.get_legend_handles_labels()
lines2, labels2 = ax6_twin.get_legend_handles_labels()
ax6.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# 7. Cross-Project Component Reusability Impact (Bottom Center)
ax7 = fig.add_subplot(gs_main[2, 1])
reusability_data = data['cross_project_reusability']

components = list(reusability_data.keys())
reuse_counts = [reusability_data[comp]['projects_count'] for comp in components]

# Create pie chart for reusability
wedges, texts, autotexts = ax7.pie(reuse_counts, labels=[c.replace('_', '\n') for c in components],
                                   autopct='%1.0f', startangle=90,
                                   colors=colors['primary_colors'][:len(components)])

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(9)

for text in texts:
    text.set_fontsize(8)

ax7.set_title('🔄 Component Reusability\nCross-Project Efficiency', fontsize=12, fontweight='bold', pad=20)

# 8. Key Business Metrics Summary (Bottom Right)
ax8 = fig.add_subplot(gs_main[2, 2])
ax8.axis('off')

# Calculate key business metrics
total_projects = len(projects)
total_users = sum([scale_info.get('peak_users', scale_info.get('monthly_active', 0))
                   for scale_info in user_scale_data.values()])
avg_project_complexity = np.mean([p['complexity'] for p in projects])
active_projects = len([p for p in projects if p['status'] == 'Ongoing'])

# Create metrics display
metrics_text = f"""
💼 BUSINESS IMPACT METRICS

🎯 Total Professional Projects: {total_projects}
👥 Combined User Impact: {total_users:,}
⭐ Average Project Complexity: {avg_project_complexity:.1f}/5
🚀 Currently Active Projects: {active_projects}

🏆 TOP PERFORMING PROJECTS:
• AI Mate & AI Seek: 200K users
• Daily Stocks: 100K users
• FT Education: 80K users
• Daency: 150K users

💡 KEY BUSINESS VALUES:
• Multi-industry expertise
• Enterprise-scale solutions
• AI/ML innovation leadership
• Government sector impact
• Educational technology focus
"""

ax8.text(0.05, 0.95, metrics_text, transform=ax8.transAxes, fontsize=11,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.5', facecolor=colors['primary_colors'][1], alpha=0.1))

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Projectwise Highlights in ND",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

# Ensure output directory exists
output_dir = os.path.join(project_dir, 'visual')
os.makedirs(output_dir, exist_ok=True)

# Save the visualization using relative path (will override existing file)
output_path = os.path.join(output_dir, 'projectwise_nd_business_impact.png')
plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#F8F9FA', edgecolor='none')

print("✅ Nerddevs Projectwise Business Impact Analysis generated successfully!")
print(f"📁 Saved to: {output_path}")
print("💼 Analysis includes: User Scale Impact, Domain Distribution, Category Analysis, Status Distribution, Tech Impact, Growth Timeline, Reusability & Business Metrics")