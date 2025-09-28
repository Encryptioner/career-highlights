import matplotlib.pyplot as plt
import pandas as pd
import json
import numpy as np
import matplotlib.gridspec as gridspec

# Set style
plt.style.use('default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

# Load the ND career data
file_path = "../graphical/diagram_ready_data.json"
with open(file_path, "r") as f:
    data = json.load(f)

# Create enhanced timeline figure
fig = plt.figure(figsize=(20, 12))
gs = gridspec.GridSpec(3, 2, figure=fig, height_ratios=[1.2, 0.8, 0.8], width_ratios=[2, 1], hspace=0.35, wspace=0.25, top=0.82)

# Define Nerddevs color scheme
colors = data["visualization_config"]["primary_colors"]
nerddevs_primary = '#FF6B6B'
nerddevs_secondary = '#4ECDC4'
bg_color = '#FAFAFA'

timeline = data["career_timeline"]
df = pd.DataFrame(timeline)

# 1. Main Career Timeline (Top Left - Large)
ax1 = fig.add_subplot(gs[0, 0])

# Create gradient background
gradient = np.linspace(0, 1, 256).reshape(256, -1)
gradient = np.vstack((gradient, gradient))
ax1.imshow(gradient, extent=[2018.5, 2025.5, 0, 10], aspect='auto', cmap='viridis', alpha=0.1)

# Plot projects as bars with gradient colors
bars = ax1.bar(df["year"], df["projects"],
               color=[colors[i] for i in range(len(df))],
               alpha=0.8, edgecolor='white', linewidth=2, width=0.6)

# Add complexity line on secondary y-axis
ax1_twin = ax1.twinx()
complexity_line = ax1_twin.plot(df["year"], df["complexity"], color=nerddevs_primary,
                               marker='D', linewidth=4, markersize=10,
                               markerfacecolor='white', markeredgecolor=nerddevs_primary,
                               markeredgewidth=3, label="Technical Complexity", zorder=10)

# Add role progression background colors
role_transitions = [(2018.5, 2021.5, nerddevs_secondary, 'Software Engineer'),
                    (2021.5, 2023.5, '#F39C12', 'Senior Software Engineer'),
                    (2023.5, 2025.5, nerddevs_primary, 'Lead Software Engineer')]

for start, end, color, role in role_transitions:
    ax1.axvspan(start, end, alpha=0.1, color=color, zorder=1)
    ax1.text((start + end) / 2, 9, role, ha='center', va='center',
            fontsize=12, fontweight='bold', color=color,
            bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.9,
                     edgecolor=color, linewidth=2))

# Add focus area annotations
for i, row in df.iterrows():
    # Add value labels on bars
    ax1.text(row["year"], row["projects"] + 0.2, str(row["projects"]),
            ha="center", va="bottom", fontsize=11, fontweight='bold', color='#2C3E50')

    # Add focus area labels
    ax1.text(row["year"], row["projects"] - 1, row["focus"],
            ha="center", va="top", fontsize=9, fontweight='bold',
            rotation=0, color='#2C3E50', wrap=True,
            bbox=dict(boxstyle="round,pad=0.3", facecolor=colors[i], alpha=0.7,
                     edgecolor='white', linewidth=1))

# Styling
ax1.set_title("Project Evolution & Technical Growth (2019-2025)",
             fontsize=16, fontweight='bold', color='#2C3E50', pad=15)
ax1.set_xlabel("Year", fontsize=14, fontweight='bold')
ax1.set_ylabel("Number of Projects", fontsize=14, fontweight='bold')
ax1_twin.set_ylabel("Technical Complexity Level", fontsize=14, fontweight='bold', color=nerddevs_primary)
ax1.grid(True, alpha=0.3, axis='y')
ax1.set_facecolor(bg_color)
ax1.set_xlim(2018.5, 2025.5)
ax1.set_ylim(0, 10)
ax1_twin.set_ylim(1, 6)

# Add legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax1_twin.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=10)

# 2. User Scale Growth (Top Right)
ax2 = fig.add_subplot(gs[0, 1])

user_years = df["year"].tolist()
user_counts = df["users"].tolist()

# Create area chart for user growth
ax2.fill_between(user_years, user_counts, alpha=0.4, color=nerddevs_primary, label='User Growth')
ax2.plot(user_years, user_counts, color=nerddevs_primary, linewidth=4, marker='o',
         markersize=10, markerfacecolor='white', markeredgecolor=nerddevs_primary, markeredgewidth=3)

# Add milestone annotations
milestones = data["user_scale_milestones"]
for milestone in milestones:
    if milestone["users"] > 0:
        ax2.annotate(f'{milestone["users"]//1000}K Users\n{milestone["milestone"]}',
                    xy=(milestone["year"], milestone["users"]),
                    xytext=(milestone["year"], milestone["users"] + 30000),
                    ha='center', fontsize=9, fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.4", facecolor=nerddevs_secondary, alpha=0.8),
                    arrowprops=dict(arrowstyle='->', color='#2C3E50', lw=2))

# Add peak highlight
peak_year = 2023
peak_users = 200000
ax2.scatter([peak_year], [peak_users], s=200, color='gold', edgecolor=nerddevs_primary,
           linewidth=3, zorder=15, label='Peak Achievement')

ax2.set_title("User Impact Scale at Nerddevs", fontsize=14, fontweight='bold', color='#2C3E50')
ax2.set_ylabel("Users Reached", fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.set_facecolor(bg_color)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K' if x > 0 else '0'))
ax2.legend(loc='upper left', fontsize=10)

# 3. Role Progression Timeline (Bottom Left)
ax3 = fig.add_subplot(gs[1, 0])

role_data = data["role_progression"]
role_df = pd.DataFrame(role_data)

# Create horizontal timeline for roles
colors_roles = [nerddevs_secondary, '#F39C12', nerddevs_primary]
start_year = 2019

for i, (_, row) in enumerate(role_df.iterrows()):
    # Draw role period rectangle
    rect = plt.Rectangle((start_year, i*1.5), row["duration"], 1,
                        facecolor=colors_roles[i], alpha=0.8, edgecolor='white', linewidth=2)
    ax3.add_patch(rect)

    # Add role text
    ax3.text(start_year + row["duration"]/2, i*1.5 + 0.5, f'{row["role"]}\n({row["years"]})',
            ha='center', va='center', fontsize=11, fontweight='bold', color='white')

    # Add focus area
    ax3.text(start_year + row["duration"] + 0.2, i*1.5 + 0.5, row["focus"],
            ha='left', va='center', fontsize=10, fontweight='bold',
            style='italic', color=colors_roles[i])

    start_year += row["duration"]

ax3.set_xlim(2018.5, 2025.5)
ax3.set_ylim(-0.5, len(role_df)*1.5)
ax3.set_title("Career Progression & Role Evolution", fontsize=14, fontweight='bold', color='#2C3E50')
ax3.set_xlabel("Years", fontsize=12, fontweight='bold')
ax3.set_yticks([])
ax3.grid(True, alpha=0.3, axis='x')
ax3.set_facecolor(bg_color)

# 4. Technology Evolution (Bottom Right)
ax4 = fig.add_subplot(gs[1, 1])

tech_evolution = data["technology_evolution"]
tech_categories = [tech["category"] for tech in tech_evolution]
latest_techs = [tech["progression"][-1] for tech in tech_evolution]

# Create horizontal bar chart for latest technologies
bars = ax4.barh(range(len(tech_categories)), [1]*len(tech_categories),
               color=colors[:len(tech_categories)], alpha=0.8,
               edgecolor='white', linewidth=2)

# Add technology labels
for i, (bar, category, latest_tech) in enumerate(zip(bars, tech_categories, latest_techs)):
    ax4.text(0.5, bar.get_y() + bar.get_height()/2,
            f"{category}:\n{latest_tech}", ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

ax4.set_title("Current Technology Stack\n(Latest Evolution)", fontsize=14, fontweight='bold', color='#2C3E50')
ax4.set_xlim(0, 1)
ax4.set_ylim(-0.5, len(tech_categories)-0.5)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_facecolor(bg_color)

# 5. Innovation Milestones (Bottom Full Width)
ax5 = fig.add_subplot(gs[2, :])

innovation_milestones = data["innovation_milestones"]
milestone_df = pd.DataFrame(innovation_milestones)

# Create timeline visualization
timeline_y = 0
for i, (_, row) in enumerate(milestone_df.iterrows()):
    color = colors[i % len(colors)]

    # Draw milestone points
    ax5.scatter(row["year"], timeline_y, s=300, color=color,
               alpha=0.9, edgecolor='white', linewidth=3, zorder=10)

    # Add milestone text with alternating positions
    y_offset = 0.4 if i % 2 == 0 else -0.4
    text_color = 'white' if i % 2 == 0 else '#2C3E50'

    ax5.annotate(row["milestone"],
                xy=(row["year"], timeline_y),
                xytext=(row["year"], y_offset),
                ha='center', va='center',
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.4", facecolor=color,
                         alpha=0.9, edgecolor='white', linewidth=2),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

# Draw main timeline
ax5.plot([2018.5, 2025.5], [timeline_y, timeline_y],
         color='#34495E', linewidth=6, alpha=0.8, zorder=5)

# Add year markers
for year in range(2019, 2026):
    ax5.axvline(x=year, color='#BDC3C7', linestyle='--', alpha=0.5, zorder=1)
    ax5.text(year, -0.7, str(year), ha='center', va='center',
            fontsize=10, fontweight='bold', color='#7F8C8D')

ax5.set_xlim(2018.5, 2025.5)
ax5.set_ylim(-0.8, 0.8)
ax5.set_title("Key Innovation & Achievement Milestones Timeline",
             fontsize=16, fontweight='bold', color='#2C3E50')
ax5.set_yticks([])
ax5.spines['left'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.spines['top'].set_visible(False)
ax5.spines['bottom'].set_visible(False)
ax5.set_facecolor(bg_color)

# Overall title
fig.suptitle("Nerddevs Career Timeline: Professional Journey & Growth Visualization",
            fontsize=20, fontweight='bold', color='#2C3E50', y=0.95)

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Yearwise Highlights in ND",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

plt.tight_layout()

# Save the timeline
output_path = "../visual/nerddevs_career_timeline.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print(f"Nerddevs career timeline saved to: {output_path}")