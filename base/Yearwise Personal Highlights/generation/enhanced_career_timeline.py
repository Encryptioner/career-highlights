import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import json
import numpy as np
from matplotlib.patches import Rectangle
import seaborn as sns

# Set style for better visuals
plt.style.use('default')
sns.set_palette("husl")

# Load the enhanced data
file_path = "../../Yearwise Highlights in ND/graphical/diagram_ready_data.json"
with open(file_path, "r") as f:
    data = json.load(f)

# Extract the career timeline data
timeline = data["career_timeline"]
df = pd.DataFrame(timeline)

# Create figure with subplots
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, height_ratios=[2, 1, 1], width_ratios=[2, 1], hspace=0.3, wspace=0.3)

# Main timeline plot
ax1 = fig.add_subplot(gs[0, :])

# Create gradient background
gradient = np.linspace(0, 1, 256).reshape(256, -1)
gradient = np.vstack((gradient, gradient))
ax1.imshow(gradient, extent=[2018.5, 2025.5, 0, 10], aspect='auto', cmap='viridis', alpha=0.1)

# Plot projects as bars with gradient effect
bars = ax1.bar(df["year"], df["projects"], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FCEA2B', '#FF9F43', '#A29BFE'],
               alpha=0.8, edgecolor='white', linewidth=2, width=0.6)

# Add gradient effect to bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    # Add a subtle gradient effect
    gradient_rect = Rectangle((bar.get_x(), 0), bar.get_width(), height,
                            facecolor=bar.get_facecolor(), alpha=0.3)
    ax1.add_patch(gradient_rect)

# Plot complexity as line with markers
line = ax1.plot(df["year"], df["complexity"], color='#E74C3C', marker='o', linewidth=4,
                markersize=10, markerfacecolor='white', markeredgecolor='#E74C3C', markeredgewidth=3,
                label="Complexity Level", zorder=10)

# Add focus areas as annotations with better styling
for i, row in df.iterrows():
    # Add focus text above bars
    ax1.text(row["year"], row["projects"] + 0.3, row["focus"],
             ha="center", va="bottom", fontsize=10, fontweight='bold',
             rotation=45, color='#2C3E50',
             bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8, edgecolor='gray'))

    # Add role information
    ax1.text(row["year"], -0.8, row["role"],
             ha="center", va="top", fontsize=9,
             rotation=45, color='#34495E', fontweight='bold')

# Customize the main plot
ax1.set_xlabel("Year", fontsize=14, fontweight='bold', color='#2C3E50')
ax1.set_ylabel("Projects Count", fontsize=14, fontweight='bold', color='#2C3E50')
ax1.set_title("Career Timeline: Projects & Complexity Evolution",
              fontsize=18, fontweight='bold', color='#2C3E50', pad=20)

# Add secondary y-axis for complexity
ax1_twin = ax1.twinx()
ax1_twin.set_ylabel("Complexity Level", fontsize=14, fontweight='bold', color='#E74C3C')
ax1_twin.set_ylim(0, 6)
ax1_twin.tick_params(axis='y', labelcolor='#E74C3C')

# Customize grid and appearance
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.set_facecolor('#FAFAFA')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_xlim(2018.5, 2025.5)
ax1.set_ylim(0, max(df["projects"]) + 2)

# Legend
legend_elements = [
    mpatches.Rectangle((0, 0), 1, 1, facecolor='#4ECDC4', alpha=0.8, label='Projects Completed'),
    plt.Line2D([0], [0], color='#E74C3C', linewidth=4, marker='o', markersize=8,
               markerfacecolor='white', markeredgecolor='#E74C3C', label='Complexity Level')
]
ax1.legend(handles=legend_elements, loc='upper left', fontsize=12, framealpha=0.9)

# Users scale subplot
ax2 = fig.add_subplot(gs[1, 0])
user_years = df["year"].tolist()
user_counts = df["users"].tolist()
colors = ['#3498DB' if users > 0 else '#BDC3C7' for users in user_counts]

bars2 = ax2.bar(user_years, user_counts, color=colors, alpha=0.8, edgecolor='white', linewidth=1)
ax2.set_title("User Scale Impact", fontsize=14, fontweight='bold', color='#2C3E50')
ax2.set_ylabel("Users Reached", fontsize=12, color='#2C3E50')
ax2.grid(True, alpha=0.3)
ax2.set_facecolor('#FAFAFA')

# Add user count labels on bars
for bar, count in zip(bars2, user_counts):
    if count > 0:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5000,
                f'{count:,}', ha='center', va='bottom', fontsize=9, fontweight='bold')

# Role progression subplot
ax3 = fig.add_subplot(gs[1, 1])
role_data = data["role_progression"]
role_df = pd.DataFrame(role_data)

# Create a horizontal timeline
y_positions = range(len(role_df))
colors_roles = ['#E74C3C', '#F39C12', '#27AE60']

for i, (idx, row) in enumerate(role_df.iterrows()):
    ax3.barh(i, row["duration"], color=colors_roles[i], alpha=0.8, height=0.6)
    ax3.text(row["duration"]/2, i, f'{row["role"]}\n({row["years"]})',
             ha='center', va='center', fontsize=9, fontweight='bold', color='white')

ax3.set_yticks(y_positions)
ax3.set_yticklabels([row["focus"] for _, row in role_df.iterrows()], fontsize=10)
ax3.set_xlabel("Years", fontsize=12, color='#2C3E50')
ax3.set_title("Role Progression", fontsize=14, fontweight='bold', color='#2C3E50')
ax3.grid(True, alpha=0.3, axis='x')
ax3.set_facecolor('#FAFAFA')

# Innovation milestones subplot
ax4 = fig.add_subplot(gs[2, :])
milestones = data["innovation_milestones"]
milestone_df = pd.DataFrame(milestones)

# Create timeline with milestones
for i, (idx, row) in enumerate(milestone_df.iterrows()):
    color = data["visualization_config"]["primary_colors"][i % len(data["visualization_config"]["primary_colors"])]
    ax4.scatter(row["year"], 0, s=300, color=color, alpha=0.8, edgecolor='white', linewidth=2, zorder=10)

    # Add milestone text
    y_offset = 0.15 if i % 2 == 0 else -0.15
    ax4.annotate(row["milestone"],
                xy=(row["year"], 0),
                xytext=(row["year"], y_offset),
                ha='center', va='center' if i % 2 == 0 else 'center',
                fontsize=9, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=color, alpha=0.7, edgecolor='white'),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

# Draw timeline line
ax4.plot([2019, 2025], [0, 0], color='#34495E', linewidth=3, alpha=0.7)
ax4.set_xlim(2018.5, 2025.5)
ax4.set_ylim(-0.4, 0.4)
ax4.set_xlabel("Year", fontsize=12, fontweight='bold', color='#2C3E50')
ax4.set_title("Innovation Milestones Timeline", fontsize=14, fontweight='bold', color='#2C3E50')
ax4.set_yticks([])
ax4.spines['left'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)
ax4.grid(True, alpha=0.3, axis='x')
ax4.set_facecolor('#FAFAFA')

# Overall styling
fig.suptitle("Comprehensive Career Highlights Dashboard",
             fontsize=24, fontweight='bold', color='#2C3E50', y=0.98)

# Add bottom note
fig.text(0.5, 0.01, "Information of Ankur Mursalin - https://encryptioner.github.io - Yearwise Personal Highlights",
         ha='center', va='bottom', fontsize=10, color='#7F8C8D', style='italic')

plt.tight_layout()

# Save the enhanced timeline
output_path = "../visual/enhanced_career_timeline.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print(f"Enhanced timeline saved to: {output_path}")