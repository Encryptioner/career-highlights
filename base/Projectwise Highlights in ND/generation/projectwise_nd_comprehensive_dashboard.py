#!/usr/bin/env python3
"""
Nerddevs Projectwise Professional Journey: Comprehensive Dashboard
Revolutionary AI & Enterprise Solutions (2019-2025)

This script generates a comprehensive professional project portfolio visualization
showcasing 18+ projects across 8 categories with enterprise impact analysis.
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import json
import seaborn as sns
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

# Create the comprehensive dashboard
fig = plt.figure(figsize=(24, 16))
fig.patch.set_facecolor('#F8F9FA')

# Create complex grid layout
gs_main = gridspec.GridSpec(4, 4, figure=fig, hspace=0.4, wspace=0.3,
                           height_ratios=[1, 0.8, 0.8, 0.6], width_ratios=[1, 1, 1, 1])

# Main title
fig.suptitle('🚀 Nerddevs Professional Project Portfolio: Revolutionary AI & Enterprise Solutions\n'
            'Comprehensive Analysis of 18+ Projects Across 8 Industry Sectors (2019-2025)',
            fontsize=20, fontweight='bold', y=0.96, color='#2C3E50')

# 1. Projects Timeline (Top Left - Large)
ax1 = fig.add_subplot(gs_main[0, :2])
projects = data['projects_timeline']
project_names = [p['name'] for p in projects]
starts = [p['start'] for p in projects]
ends = [p['end'] for p in projects]
complexities = [p['complexity'] for p in projects]
categories = [p['category'] for p in projects]

# Create timeline visualization
y_positions = range(len(projects))
for i, (project, start, end, complexity, category) in enumerate(zip(project_names, starts, ends, complexities, categories)):
    duration = end - start
    color = colors['category_colors'].get(category, colors['primary_colors'][i % len(colors['primary_colors'])])

    # Draw project bar with complexity-based alpha
    alpha = 0.6 + (complexity * 0.08)
    ax1.barh(i, duration, left=start, height=0.6, color=color, alpha=alpha, edgecolor='white')

    # Add project name and complexity
    ax1.text(start + duration/2, i, f'{project}\n(Level {complexity})',
             ha='center', va='center', fontsize=8, fontweight='bold', color='white')

ax1.set_yticks(y_positions)
ax1.set_yticklabels(project_names, fontsize=9)
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_title('🎯 Professional Project Timeline: AI & Enterprise Solutions Evolution', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlim(2018.5, 2025.5)
ax1.grid(True, alpha=0.3, axis='x')

# Add gradient background
gradient = np.linspace(0, 1, 256).reshape(256, -1)
gradient = np.vstack((gradient, gradient))
ax1.imshow(gradient, extent=[2018.5, 2025.5, -1, len(projects)], aspect='auto', cmap='Blues', alpha=0.1)

# 2. Category Distribution (Top Right)
ax2 = fig.add_subplot(gs_main[0, 2:])
categories_data = data['project_categories']
category_names = list(categories_data.keys())
category_counts = [categories_data[cat]['count'] for cat in category_names]
category_colors = [colors['category_colors'].get(cat, colors['primary_colors'][i])
                   for i, cat in enumerate(category_names)]

# Create enhanced pie chart
wedges, texts, autotexts = ax2.pie(category_counts, labels=category_names, autopct='%1.1f%%',
                                   startangle=90, colors=category_colors, explode=[0.05] * len(category_names))

# Enhance pie chart appearance
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

ax2.set_title('📊 Project Distribution by Category\nComprehensive Professional Portfolio',
              fontsize=14, fontweight='bold', pad=20)

# 3. Technology Stack Evolution (Second Row Left)
ax3 = fig.add_subplot(gs_main[1, :2])
tech_data = data['technology_stack_usage']

# Prepare data for stacked area chart
years = list(range(2019, 2026))
tech_categories = ['Frontend', 'Backend', 'Databases', 'Mobile', 'AI_ML']
category_totals = {cat: [] for cat in tech_categories}

for year in years:
    for cat in tech_categories:
        if cat in tech_data:
            total = sum(1 for tech, info in tech_data[cat].items() if year in info['years'])
            category_totals[cat].append(total)
        else:
            category_totals[cat].append(0)

# Create stacked area chart
ax3.stackplot(years, *[category_totals[cat] for cat in tech_categories],
              labels=tech_categories, alpha=0.8, colors=colors['primary_colors'][:len(tech_categories)])

ax3.set_xlabel('Year', fontsize=12, fontweight='bold')
ax3.set_ylabel('Technologies Used', fontsize=12, fontweight='bold')
ax3.set_title('⚡ Technology Stack Evolution: Professional Growth Trajectory', fontsize=14, fontweight='bold', pad=20)
ax3.legend(loc='upper left', fontsize=10)
ax3.grid(True, alpha=0.3)

# 4. Complexity vs Impact Analysis (Second Row Right)
ax4 = fig.add_subplot(gs_main[1, 2:])
user_scale_data = data['user_scale_by_project']
project_complexities = {p['name']: p['complexity'] for p in projects}

# Prepare bubble chart data
project_names_bubble = []
complexities_bubble = []
user_impacts = []
categories_bubble = []

for project_name, scale_info in user_scale_data.items():
    if project_name in project_complexities:
        project_names_bubble.append(project_name[:15])  # Truncate for display
        complexities_bubble.append(project_complexities[project_name])

        # Extract user impact (use different keys as available)
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
        categories_bubble.append(scale_info['category'])

# Create bubble chart
for i, (name, complexity, impact, category) in enumerate(zip(project_names_bubble, complexities_bubble, user_impacts, categories_bubble)):
    color = colors['category_colors'].get(category.split()[0] if ' ' in category else category,
                                         colors['primary_colors'][i % len(colors['primary_colors'])])
    ax4.scatter(complexity, impact, s=impact/500 + 100, alpha=0.7, c=color, edgecolors='white', linewidth=2)
    ax4.annotate(name, (complexity, impact), xytext=(5, 5), textcoords='offset points',
                fontsize=8, fontweight='bold')

ax4.set_xlabel('Project Complexity Level', fontsize=12, fontweight='bold')
ax4.set_ylabel('User Impact Scale', fontsize=12, fontweight='bold')
ax4.set_title('💫 Complexity vs Impact: Professional Project Analysis', fontsize=14, fontweight='bold', pad=20)
ax4.grid(True, alpha=0.3)
ax4.set_yscale('log')

# 5. Architecture Evolution (Third Row Left)
ax5 = fig.add_subplot(gs_main[2, :2])
arch_data = data['development_methodology_evolution']['Architecture_Patterns']

periods = [entry['period'] for entry in arch_data]
patterns = [entry['pattern'] for entry in arch_data]
project_counts = [len(entry['projects']) for entry in arch_data]

# Create evolution timeline
x_positions = range(len(periods))
bars = ax5.bar(x_positions, project_counts, color=colors['primary_colors'][:len(periods)],
               alpha=0.8, edgecolor='white', linewidth=2)

# Add pattern labels on bars
for i, (bar, pattern, count) in enumerate(zip(bars, patterns, project_counts)):
    ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            f'{pattern}\n({count} projects)', ha='center', va='bottom',
            fontsize=9, fontweight='bold')

ax5.set_xticks(x_positions)
ax5.set_xticklabels(periods, rotation=45, ha='right')
ax5.set_ylabel('Number of Projects', fontsize=12, fontweight='bold')
ax5.set_title('🏗️ Architecture Pattern Evolution: Professional Methodology Growth', fontsize=14, fontweight='bold', pad=20)
ax5.grid(True, alpha=0.3, axis='y')

# 6. Cross-Project Reusability (Third Row Right)
ax6 = fig.add_subplot(gs_main[2, 2:])
reusability_data = data['cross_project_reusability']

components = list(reusability_data.keys())
reuse_counts = [reusability_data[comp]['projects_count'] for comp in components]

# Create horizontal bar chart
y_positions = range(len(components))
bars = ax6.barh(y_positions, reuse_counts, color=colors['primary_colors'][:len(components)],
                alpha=0.8, edgecolor='white', linewidth=2)

# Add count labels
for bar, count in zip(bars, reuse_counts):
    ax6.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
            str(count), va='center', fontweight='bold', fontsize=10)

ax6.set_yticks(y_positions)
ax6.set_yticklabels([comp.replace('_', ' ') for comp in components], fontsize=10)
ax6.set_xlabel('Projects Using Component', fontsize=12, fontweight='bold')
ax6.set_title('🔄 Cross-Project Component Reusability Analysis', fontsize=14, fontweight='bold', pad=20)
ax6.grid(True, alpha=0.3, axis='x')

# 7. Business Domain Impact (Bottom Left)
ax7 = fig.add_subplot(gs_main[3, :2])
domain_data = data['business_domain_distribution']

domains = list(domain_data.keys())
project_counts = [domain_data[domain]['projects'] for domain in domains]
complexities = [domain_data[domain]['complexity'] for domain in domains]

# Create scatter plot with size representing complexity
for i, (domain, count, complexity) in enumerate(zip(domains, project_counts, complexities)):
    color = colors['primary_colors'][i % len(colors['primary_colors'])]
    ax7.scatter(count, complexity, s=complexity*80, alpha=0.7, c=color, edgecolors='white', linewidth=2)
    ax7.annotate(domain.replace('_', ' '), (count, complexity), xytext=(5, 5),
                textcoords='offset points', fontsize=9, fontweight='bold')

ax7.set_xlabel('Number of Projects', fontsize=12, fontweight='bold')
ax7.set_ylabel('Average Complexity', fontsize=12, fontweight='bold')
ax7.set_title('🌐 Business Domain Impact: Professional Specialization Analysis', fontsize=14, fontweight='bold', pad=20)
ax7.grid(True, alpha=0.3)

# 8. Key Metrics Summary (Bottom Right)
ax8 = fig.add_subplot(gs_main[3, 2:])
ax8.axis('off')

# Calculate key metrics
total_projects = len(data['projects_timeline'])
total_categories = len(data['project_categories'])
max_users = max([scale_info.get('peak_users', scale_info.get('monthly_active', scale_info.get('active_users', 0)))
                 for scale_info in data['user_scale_by_project'].values()])
avg_complexity = np.mean([p['complexity'] for p in data['projects_timeline']])

# Create metrics display
metrics_text = f"""
🎯 PROFESSIONAL PROJECT PORTFOLIO METRICS

📊 Total Projects: {total_projects}
🏢 Industry Categories: {total_categories}
👥 Peak User Impact: {max_users:,}
⭐ Average Complexity: {avg_complexity:.1f}/5
🚀 Active Period: 2019-2025
💼 Professional Focus: AI & Enterprise Solutions

🔥 Revolutionary Projects:
• AI Mate & AI Seek (200K users)
• Bikribatta ERP (Enterprise scale)
• Biddaan (Multi-company SaaS)

⚡ Technology Excellence:
• React/Vue.js Frontend Mastery
• Node.js/NestJS Backend Leadership
• MongoDB/PostgreSQL Database Design
• OpenAI API Integration Pioneer
"""

ax8.text(0.05, 0.95, metrics_text, transform=ax8.transAxes, fontsize=11,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.5', facecolor=colors['primary_colors'][0], alpha=0.1))

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Projectwise Highlights in ND",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

# Ensure output directory exists
output_dir = os.path.join(project_dir, 'visual')
os.makedirs(output_dir, exist_ok=True)

# Save the visualization using relative path (will override existing file)
output_path = os.path.join(output_dir, 'projectwise_nd_comprehensive_dashboard.png')
plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#F8F9FA', edgecolor='none')

print("✅ Nerddevs Projectwise Comprehensive Dashboard generated successfully!")
print(f"📁 Saved to: {output_path}")
print("🎯 Dashboard includes: Timeline, Categories, Technology Evolution, Impact Analysis, Architecture Evolution, Reusability, Domain Impact & Key Metrics")