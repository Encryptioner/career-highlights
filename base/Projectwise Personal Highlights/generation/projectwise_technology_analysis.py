import matplotlib.pyplot as plt
import pandas as pd
import json
from math import pi
import seaborn as sns
from matplotlib.patches import Wedge, Circle
from collections import Counter

# Set style
plt.style.use('default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

# Load the project data
file_path = "../graphical/diagram_ready_data.json"
with open(file_path, "r") as f:
    data = json.load(f)

# Create technology analysis figure
fig = plt.figure(figsize=(20, 14))
gs = fig.add_gridspec(3, 3, height_ratios=[1, 1, 0.8], width_ratios=[1, 1, 1], hspace=0.35, wspace=0.3, top=0.82)

# Define color scheme
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FCEA2B', '#FF9F43', '#A29BFE', '#6C5CE7', '#FD79A8', '#00CEC9']
primary_color = '#FF6B6B'
secondary_color = '#4ECDC4'
bg_color = '#FAFAFA'

projects_timeline = data["projects_timeline"]
df = pd.DataFrame(projects_timeline)

# 1. Technology Usage Radar Chart (Top Left)
ax1 = fig.add_subplot(gs[0, 0], projection='polar')

# Count all technologies across projects
all_technologies = []
for _, project in df.iterrows():
    all_technologies.extend(project["tech"])

# Get top technologies by usage
tech_counter = Counter(all_technologies)
top_technologies = dict(tech_counter.most_common(12))

# Create radar chart
categories = list(top_technologies.keys())
values = list(top_technologies.values())
N = len(categories)

# Compute angle for each axis
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]  # Complete the circle

# Close the plot
values += values[:1]

# Plot
ax1.set_theta_offset(pi / 2)
ax1.set_theta_direction(-1)

# Draw the radar
ax1.plot(angles, values, 'o-', linewidth=3, color=primary_color, markersize=8,
         markerfacecolor='white', markeredgecolor=primary_color, markeredgewidth=2)
ax1.fill(angles, values, alpha=0.25, color=primary_color)

# Add category labels
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=10, fontweight='bold')
ax1.set_ylim(0, max(values) + 1)
ax1.grid(True, alpha=0.3)

ax1.set_title("Technology Usage\nFrequency Radar", fontsize=14, fontweight='bold',
              color='#2C3E50', pad=20)

# 2. Technology Evolution by Year (Top Center)
ax2 = fig.add_subplot(gs[0, 1])

# Create technology evolution heatmap
tech_by_year = {}
for _, project in df.iterrows():
    year = project["year"]
    if year not in tech_by_year:
        tech_by_year[year] = []
    tech_by_year[year].extend(project["tech"])

# Get unique technologies and years
all_years = sorted(tech_by_year.keys())
unique_techs = list(set(all_technologies))

# Create matrix for heatmap
matrix = []
tech_labels = []

# Use top 15 technologies for better visualization
top_15_techs = [tech for tech, count in tech_counter.most_common(15)]

for tech in top_15_techs:
    tech_years = []
    for year in all_years:
        if tech in tech_by_year.get(year, []):
            tech_years.append(1)
        else:
            tech_years.append(0)
    matrix.append(tech_years)
    tech_labels.append(tech)

# Create heatmap
sns.heatmap(matrix, xticklabels=all_years, yticklabels=tech_labels,
           cmap='YlOrRd', cbar_kws={'label': 'Technology Used'},
           ax=ax2, square=False, linewidths=1, cbar=True)

ax2.set_title("Technology Evolution\nHeatmap by Year", fontsize=14, fontweight='bold', color='#2C3E50')
ax2.set_xlabel("Year", fontsize=12, fontweight='bold')
ax2.tick_params(axis='y', labelsize=9)
ax2.tick_params(axis='x', rotation=0)

# 3. Project Categories vs Technology Diversity (Top Right)
ax3 = fig.add_subplot(gs[0, 2])

# Calculate technology diversity by category
category_tech_diversity = {}
category_projects = df.groupby('category')
for category, group in category_projects:
    unique_techs_in_category = set()
    for _, project in group.iterrows():
        unique_techs_in_category.update(project["tech"])
    category_tech_diversity[category] = {
        'tech_count': len(unique_techs_in_category),
        'project_count': len(group),
        'avg_complexity': group['complexity'].mean()
    }

categories = list(category_tech_diversity.keys())
tech_counts = [category_tech_diversity[cat]['tech_count'] for cat in categories]
project_counts = [category_tech_diversity[cat]['project_count'] for cat in categories]
avg_complexities = [category_tech_diversity[cat]['avg_complexity'] for cat in categories]

# Create bubble chart
for i, (cat, tech_count, proj_count, avg_comp) in enumerate(zip(categories, tech_counts, project_counts, avg_complexities)):
    ax3.scatter(tech_count, avg_comp, s=proj_count * 150,
               color=colors[i % len(colors)], alpha=0.7,
               edgecolors='white', linewidths=2)

    # Add category labels
    ax3.annotate(cat[:12] + "..." if len(cat) > 12 else cat,
                xy=(tech_count, avg_comp),
                xytext=(5, 5), textcoords='offset points',
                fontsize=9, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=colors[i % len(colors)], alpha=0.8),
                color='white')

ax3.set_title("Categories: Tech Diversity vs Complexity\n(Bubble Size = Project Count)",
             fontsize=14, fontweight='bold', color='#2C3E50')
ax3.set_xlabel("Technology Diversity", fontsize=12, fontweight='bold')
ax3.set_ylabel("Average Complexity", fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.set_facecolor(bg_color)

# 4. Framework Evolution Timeline (Middle Left)
ax4 = fig.add_subplot(gs[1, 0])

frameworks_data = data["technology_evolution"]["frameworks"]

# Create stacked timeline
y_base = 0
for i, fw_period in enumerate(frameworks_data):
    period = fw_period["period"]
    frameworks = fw_period["frameworks"]
    complexity = fw_period["complexity"]

    # Draw period block
    height = len(frameworks) * 0.5
    rect = plt.Rectangle((i - 0.4, y_base), 0.8, height,
                        facecolor=colors[i % len(colors)], alpha=0.8,
                        edgecolor='white', linewidth=2)
    ax4.add_patch(rect)

    # Add framework names
    for j, framework in enumerate(frameworks):
        ax4.text(i, y_base + j * 0.5 + 0.25, framework,
                ha='center', va='center', fontsize=9, fontweight='bold',
                color='white')

    # Add period label
    ax4.text(i, y_base - 0.3, period, ha='center', va='center',
            fontsize=10, fontweight='bold', color=colors[i % len(colors)])

    # Add complexity label
    ax4.text(i, y_base + height + 0.1, complexity, ha='center', va='center',
            fontsize=9, style='italic', color='#2C3E50')

    y_base = 0  # Reset for side-by-side layout

ax4.set_xlim(-0.8, len(frameworks_data))
ax4.set_ylim(-0.8, max(len(fw["frameworks"]) for fw in frameworks_data) * 0.5 + 1)
ax4.set_title("Framework Evolution\nby Time Period", fontsize=14, fontweight='bold', color='#2C3E50')
ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_facecolor(bg_color)

# 5. Programming Language Progression (Middle Center)
ax5 = fig.add_subplot(gs[1, 1])

languages_data = data["technology_evolution"]["languages"]

# Create language progression flow
for i, lang_data in enumerate(languages_data):
    year = lang_data["year"]
    primary = lang_data["primary"]
    secondary = lang_data["secondary"]
    focus = lang_data["focus"]

    # Draw primary language circle
    ax5.scatter(i, 1, s=300, color=colors[i % len(colors)],
               alpha=0.9, edgecolor='white', linewidth=3, zorder=10)
    ax5.text(i, 1, primary[:8], ha='center', va='center',
            fontsize=9, fontweight='bold', color='white')

    # Draw secondary languages
    if secondary:
        for j, sec_lang in enumerate(secondary[:2]):  # Show max 2 secondary
            ax5.scatter(i, 0.4 - j * 0.3, s=150,
                       color=colors[i % len(colors)], alpha=0.6,
                       edgecolor='white', linewidth=2)
            ax5.text(i, 0.4 - j * 0.3, sec_lang[:6], ha='center', va='center',
                    fontsize=7, fontweight='bold', color='white')

    # Add year and focus
    ax5.text(i, 1.5, str(year), ha='center', va='center',
            fontsize=11, fontweight='bold', color='#2C3E50')
    ax5.text(i, -0.5, focus[:15] + "..." if len(focus) > 15 else focus,
            ha='center', va='center', fontsize=8, style='italic',
            color='#7F8C8D', wrap=True)

    # Connect to next year
    if i < len(languages_data) - 1:
        ax5.arrow(i + 0.15, 1, 0.7, 0, head_width=0.05, head_length=0.08,
                 fc='#BDC3C7', ec='#BDC3C7', alpha=0.7)

ax5.set_xlim(-0.5, len(languages_data))
ax5.set_ylim(-0.8, 1.8)
ax5.set_title("Programming Language\nProgression", fontsize=14, fontweight='bold', color='#2C3E50')
ax5.set_xticks([])
ax5.set_yticks([])
ax5.set_facecolor(bg_color)

# 6. Technology Specializations Radar (Middle Right)
ax6 = fig.add_subplot(gs[1, 2], projection='polar')

specializations = data["technology_evolution"]["specializations"]

# Group specializations by domain
spec_domains = {}
for spec in specializations:
    specialization = spec["specialization"]
    # Categorize specializations
    if "Machine Learning" in specialization or "Computer" in specialization:
        domain = "AI/ML"
    elif "Web Development" in specialization or "Architecture" in specialization:
        domain = "Web/Architecture"
    elif "Programming" in specialization or "Systems" in specialization:
        domain = "Systems"
    elif "Real-time" in specialization or "WebSocket" in specialization:
        domain = "Real-time"
    elif "TypeScript" in specialization or "Enterprise" in specialization:
        domain = "Enterprise"
    elif "Performance" in specialization or "Design" in specialization:
        domain = "Performance"
    elif "AI" in specialization or "WebAssembly" in specialization:
        domain = "Modern AI"
    else:
        domain = "General"

    if domain not in spec_domains:
        spec_domains[domain] = 0
    spec_domains[domain] += 1

# Create radar for specialization domains
spec_categories = list(spec_domains.keys())
spec_values = list(spec_domains.values())
N_spec = len(spec_categories)

angles_spec = [n / float(N_spec) * 2 * pi for n in range(N_spec)]
angles_spec += angles_spec[:1]
spec_values += spec_values[:1]

ax6.plot(angles_spec, spec_values, 'o-', linewidth=3, color=secondary_color,
         markersize=8, markerfacecolor='white', markeredgecolor=secondary_color, markeredgewidth=2)
ax6.fill(angles_spec, spec_values, alpha=0.25, color=secondary_color)

ax6.set_xticks(angles_spec[:-1])
ax6.set_xticklabels(spec_categories, fontsize=10, fontweight='bold')
ax6.set_ylim(0, max(spec_values) + 1)
ax6.grid(True, alpha=0.3)

ax6.set_title("Specialization Domains\nRadar", fontsize=14, fontweight='bold',
              color='#2C3E50', pad=20)

# 7. Cross-Project Technology Reusability (Bottom Left)
ax7 = fig.add_subplot(gs[2, 0])

reusability_data = data["cross_project_reusability"]

# Extract reusability metrics
reuse_categories = list(reusability_data.keys())
reuse_projects = [reusability_data[cat]["projects"] for cat in reuse_categories]
evolutions = [reusability_data[cat]["evolution"] for cat in reuse_categories]

# Create horizontal bar chart
bars = ax7.barh(range(len(reuse_categories)), reuse_projects,
                color=colors[:len(reuse_categories)], alpha=0.8,
                edgecolor='white', linewidth=2)

# Add evolution annotations
for i, (bar, evolution, projects) in enumerate(zip(bars, evolutions, reuse_projects)):
    # Add project count
    ax7.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
             str(projects), va='center', fontsize=11, fontweight='bold')

    # Add evolution text
    ax7.text(bar.get_width() * 0.5, bar.get_y() + bar.get_height()/2,
             evolution.split(' → ')[-1],  # Show final evolution stage
             va='center', ha='center', fontsize=8, fontweight='bold',
             color='white')

ax7.set_yticks(range(len(reuse_categories)))
readable_reuse = [cat.replace('_', ' ').title() for cat in reuse_categories]
ax7.set_yticklabels(readable_reuse, fontsize=10)
ax7.set_title("Cross-Project Technology\nReusability", fontsize=14, fontweight='bold', color='#2C3E50')
ax7.set_xlabel("Projects Using Technology", fontsize=12, fontweight='bold')
ax7.grid(True, alpha=0.3, axis='x')
ax7.set_facecolor(bg_color)

# 8. Technology Adoption Timeline (Bottom Center)
ax8 = fig.add_subplot(gs[2, 1])

# Create adoption timeline showing when each major technology was first used
first_usage = {}
for _, project in df.iterrows():
    year = project["year"]
    for tech in project["tech"]:
        if tech not in first_usage:
            first_usage[tech] = year

# Sort by adoption year
adoption_timeline = sorted(first_usage.items(), key=lambda x: x[1])

# Group technologies by year for better visualization
adoption_by_year = {}
for tech, year in adoption_timeline:
    if year not in adoption_by_year:
        adoption_by_year[year] = []
    adoption_by_year[year].append(tech)

# Create timeline visualization
for i, (year, techs) in enumerate(sorted(adoption_by_year.items())):
    # Draw year marker
    ax8.scatter(year, 0, s=len(techs) * 50, color=colors[i % len(colors)],
               alpha=0.8, edgecolor='white', linewidth=2, zorder=10)

    # Add technology count
    ax8.text(year, 0, str(len(techs)), ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # Add sample technologies
    sample_techs = techs[:3]  # Show max 3 technologies
    if len(techs) > 3:
        sample_techs.append(f"+{len(techs)-3} more")

    tech_text = "\n".join(sample_techs)
    y_offset = 0.4 if i % 2 == 0 else -0.4
    ax8.annotate(tech_text,
                xy=(year, 0), xytext=(year, y_offset),
                ha='center', va='center', fontsize=8, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=colors[i % len(colors)], alpha=0.8),
                arrowprops=dict(arrowstyle='->', color=colors[i % len(colors)]),
                color='white')

# Draw timeline
years_sorted = sorted(adoption_by_year.keys())
ax8.plot([years_sorted[0] - 0.5, years_sorted[-1] + 0.5], [0, 0],
         color='#34495E', linewidth=4, alpha=0.7, zorder=5)

ax8.set_xlim(years_sorted[0] - 1, years_sorted[-1] + 1)
ax8.set_ylim(-0.8, 0.8)
ax8.set_title("Technology Adoption\nTimeline", fontsize=14, fontweight='bold', color='#2C3E50')
ax8.set_xlabel("Year First Used", fontsize=12, fontweight='bold')
ax8.set_yticks([])
ax8.grid(True, alpha=0.3, axis='x')
ax8.set_facecolor(bg_color)

# 9. Modern Technology Focus (Bottom Right)
ax9 = fig.add_subplot(gs[2, 2])

# Focus on 2024-2025 technologies (modern innovations)
modern_projects = df[df["year"] >= 2024]
modern_technologies = []
for _, project in modern_projects.iterrows():
    modern_technologies.extend(project["tech"])

modern_tech_counter = Counter(modern_technologies)
top_modern_techs = dict(modern_tech_counter.most_common(8))

# Create donut chart
if top_modern_techs:
    tech_names = list(top_modern_techs.keys())
    tech_counts = list(top_modern_techs.values())

    wedges, texts, autotexts = ax9.pie(tech_counts, labels=None,
                                       colors=colors[:len(tech_names)],
                                       autopct='%1.0f', startangle=90,
                                       textprops={'fontsize': 10, 'fontweight': 'bold'},
                                       pctdistance=0.85, wedgeprops=dict(width=0.6))

    # Add center circle
    centre_circle = Circle((0,0), 0.4, fc='white', linewidth=2, edgecolor='#2C3E50')
    ax9.add_artist(centre_circle)
    ax9.text(0, 0, '2024-2025\nModern\nTech', ha='center', va='center',
            fontsize=11, fontweight='bold', color='#2C3E50')

    # Create legend
    ax9.legend(wedges, tech_names, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9)

ax9.set_title("Modern Technology\nFocus (2024-2025)", fontsize=14, fontweight='bold', color='#2C3E50')

# Overall styling and title
fig.suptitle("Personal Projects Technology Analysis: Skills Evolution & Innovation Patterns",
            fontsize=18, fontweight='bold', color='#2C3E50', y=0.95)

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Projectwise Personal Highlights",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

plt.tight_layout()

# Save the technology analysis
output_path = "../visual/projectwise_technology_analysis.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print(f"Projectwise technology analysis saved to: {output_path}")