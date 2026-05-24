import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Create a Data Flow Diagram using Plotly with improved layout
fig = go.Figure()

# Define positions for a cleaner layout
# External entities (left and right)
external_positions = {
    'User/Adopter': (1, 6),
    'Admin': (1, 3),
    'Database': (9, 4.5)
}

# Processes (center area) - arranged in 2 columns
process_positions = {
    'P1': (3.5, 7),    # User Registration/Login
    'P2': (3.5, 5.5),  # Browse Animals  
    'P3': (3.5, 4),    # Submit Adoption Application
    'P4': (5.5, 7),    # Admin Management
    'P5': (5.5, 5.5),  # Animal Management
    'P6': (5.5, 4)     # Application Processing
}

# Data stores (right side)
datastore_positions = {
    'User Database': (7.5, 6.5),
    'Animal Database': (7.5, 5),
    'Application Database': (7.5, 3.5)
}

# Add external entities
for name, pos in external_positions.items():
    fig.add_trace(go.Scatter(
        x=[pos[0]], 
        y=[pos[1]],
        mode='markers+text',
        marker=dict(size=100, color='#1FB8CD', symbol='square', line=dict(width=3, color='#13343B')),
        text=[name],
        textposition='middle center',
        textfont=dict(size=11, color='white'),
        name='External Entities' if name == 'User/Adopter' else '',
        showlegend=True if name == 'User/Adopter' else False,
        legendgroup='entities'
    ))

# Add processes as circles
process_labels = {
    'P1': '1. User Reg',
    'P2': '2. Browse',  
    'P3': '3. Submit App',
    'P4': '4. Admin Mgmt',
    'P5': '5. Animal Mgmt',
    'P6': '6. App Process'
}

for pid, pos in process_positions.items():
    fig.add_trace(go.Scatter(
        x=[pos[0]], 
        y=[pos[1]],
        mode='markers+text',
        marker=dict(size=90, color='#DB4545', symbol='circle', line=dict(width=3, color='#B4413C')),
        text=[process_labels[pid]],
        textposition='middle center',
        textfont=dict(size=10, color='white'),
        name='Processes' if pid == 'P1' else '',
        showlegend=True if pid == 'P1' else False,
        legendgroup='processes'
    ))

# Add data stores
for name, pos in datastore_positions.items():
    # Shorten names for display
    display_name = name.replace('Database', 'DB')
    fig.add_trace(go.Scatter(
        x=[pos[0]], 
        y=[pos[1]],
        mode='markers+text',
        marker=dict(size=100, color='#2E8B57', symbol='square', line=dict(width=3, color='#13343B')),
        text=[display_name],
        textposition='middle center',
        textfont=dict(size=11, color='white'),
        name='Data Stores' if name == 'User Database' else '',
        showlegend=True if name == 'User Database' else False,
        legendgroup='datastores'
    ))

# Define data flows from the JSON data
data_flows = [
    # From User/Adopter
    (external_positions['User/Adopter'], process_positions['P1'], 'Reg Info'),
    (external_positions['User/Adopter'], process_positions['P2'], 'Search'),
    (external_positions['User/Adopter'], process_positions['P3'], 'App Form'),
    
    # From Admin
    (external_positions['Admin'], process_positions['P4'], 'Commands'),
    (external_positions['Admin'], process_positions['P5'], 'Animal Data'),
    (external_positions['Admin'], process_positions['P6'], 'Approval'),
    
    # Process to Data Store
    (process_positions['P1'], datastore_positions['User Database'], 'User Details'),
    (process_positions['P2'], datastore_positions['Animal Database'], 'Query'),
    (process_positions['P3'], datastore_positions['Application Database'], 'App Data'),
    (process_positions['P5'], datastore_positions['Animal Database'], 'CRUD Ops'),
    (process_positions['P6'], datastore_positions['Application Database'], 'Updates'),
    
    # Data Store to Process
    (datastore_positions['Animal Database'], process_positions['P2'], 'Animal List'),
    
    # Process to External Entity
    (process_positions['P2'], external_positions['User/Adopter'], 'Details')
]

# Add arrows with better positioning
for i, (start, end, label) in enumerate(data_flows):
    # Add arrow
    fig.add_annotation(
        x=end[0], y=end[1],
        ax=start[0], ay=start[1],
        xref='x', yref='y',
        axref='x', ayref='y',
        text='',
        showarrow=True,
        arrowhead=2,
        arrowsize=1.2,
        arrowwidth=2,
        arrowcolor='#5D878F'
    )
    
    # Position label offset from arrow midpoint to avoid clutter
    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2
    
    # Offset label slightly to avoid overlap
    offset_x = 0.15 if i % 2 == 0 else -0.15
    offset_y = 0.1 if i % 3 == 0 else -0.1
    
    fig.add_annotation(
        x=mid_x + offset_x, 
        y=mid_y + offset_y,
        text=label,
        showarrow=False,
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='#5D878F',
        borderwidth=1,
        font=dict(size=9, color='#13343B'),
        yanchor='middle',
        xanchor='center'
    )

# Update layout with better spacing
fig.update_layout(
    title='Animal Adoption System DFD Level 0',
    xaxis=dict(
        showgrid=False, 
        showticklabels=False, 
        zeroline=False, 
        range=[0, 10]
    ),
    yaxis=dict(
        showgrid=False, 
        showticklabels=False, 
        zeroline=False, 
        range=[2.5, 8]
    ),
    showlegend=True,
    legend=dict(
        orientation='h', 
        yanchor='bottom', 
        y=1.05, 
        xanchor='center', 
        x=0.5
    ),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Save the chart
fig.write_image("dfd_level0.png")
fig.write_image("dfd_level0.svg", format="svg")

print("Improved DFD Level 0 created successfully!")