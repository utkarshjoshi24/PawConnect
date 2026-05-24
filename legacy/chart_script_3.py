import plotly.graph_objects as go
import json

# Parse the provided data
data = {"problems": [{"issue": "Limited Database Coverage", "description": "Most platforms only display a small subset of available animals"}, {"issue": "Poor User Interface", "description": "Overcomplicated layouts discourage potential adopters"}, {"issue": "No Real-Time Updates", "description": "Adopted animals remain visible, causing confusion"}, {"issue": "Weak Data Management", "description": "Insecure and unstructured data storage"}, {"issue": "No Local Connectivity", "description": "Lack of nearby shelter or hospital integration"}, {"issue": "Limited Functionality", "description": "Poor tracking of the adoption process"}, {"issue": "Lack of Awareness", "description": "Minimal educational or welfare resources"}], "solutions": [{"feature": "Centralized Animal Database", "description": "All available animals from multiple shelters in one place"}, {"feature": "User-Friendly Interface", "description": "Clean, intuitive HTML/CSS design with easy navigation"}, {"feature": "Real-Time Database Sync", "description": "SQLite database updates instantly reflect adoption status"}, {"feature": "Secure Data Storage", "description": "SQLite with C backend ensures secure, structured data"}, {"feature": "Location-Based Features", "description": "Integration with nearby shelters and veterinary hospitals"}, {"feature": "Complete CRUD Operations", "description": "Full animal and adoption management capabilities"}, {"feature": "Educational Resources", "description": "Information on pet care and adoption guidance"}]}

# Prepare data for table with clear symbols and better formatting
problems = []
solutions = []

for item in data['problems']:
    # Use clear red X symbol and format text properly
    problems.append(f"❌  {item['issue']}\n{item['description']}")

for item in data['solutions']:
    # Use clear green checkmark symbol and format text properly
    solutions.append(f"✅  {item['feature']}\n{item['description']}")

# Create table with improved styling and spacing
fig = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Current System Problems</b>', '<b>Proposed Solution Features</b>'],
        fill_color='#1FB8CD',
        align='center',
        font=dict(color='white', size=18, family='Arial'),
        height=70
    ),
    cells=dict(
        values=[problems, solutions],
        fill_color=[['#FFCDD2'] * len(problems), ['#A5D6A7'] * len(solutions)],
        align='left',
        font=dict(color='black', size=14, family='Arial'),
        height=100,
        line_color='white',
        line_width=3
    )
)])

fig.update_layout(
    title="Animal Adoption System Comparison",
    showlegend=False,
    font=dict(family='Arial')
)

# Save as both PNG and SVG
fig.write_image("comparison_table.png")
fig.write_image("comparison_table.svg", format="svg")