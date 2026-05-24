# Create an Entity Relationship Diagram for the animal adoption database using plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Entity data with attributes
entities = {
    'Shelters': {
        'pos': (0, 4),
        'attributes': ['id (PK)', 'name', 'address', 'phone', 'email', 'capacity'],
        'color': '#1FB8CD'
    },
    'Animals': {
        'pos': (2, 4),
        'attributes': ['id (PK)', 'name', 'species', 'breed', 'age', 'gender', 
                      'health_status', 'status', 'description', 'image_url', 
                      'shelter_id (FK)', 'date_added'],
        'color': '#DB4545'
    },
    'Users': {
        'pos': (0, 2),
        'attributes': ['id (PK)', 'name', 'email', 'password', 'phone', 
                      'address', 'city', 'registration_date'],
        'color': '#2E8B57'
    },
    'Adoptions': {
        'pos': (2, 2),
        'attributes': ['id (PK)', 'user_id (FK)', 'animal_id (FK)', 
                      'application_date', 'status', 'approval_date', 'notes'],
        'color': '#5D878F'
    },
    'Admins': {
        'pos': (1, 0),
        'attributes': ['id (PK)', 'username', 'password', 'email', 'role', 'created_date'],
        'color': '#D2BA4C'
    }
}

# Relationships
relationships = [
    ('Shelters', 'Animals', '1:N'),
    ('Users', 'Adoptions', '1:N'),
    ('Animals', 'Adoptions', '1:N')
]

fig = go.Figure()

# Add relationship lines first (so they appear behind entities)
for rel in relationships:
    entity1, entity2, cardinality = rel
    x1, y1 = entities[entity1]['pos']
    x2, y2 = entities[entity2]['pos']
    
    # Add relationship line
    fig.add_trace(go.Scatter(
        x=[x1, x2], y=[y1, y2],
        mode='lines',
        line=dict(color='#13343B', width=2),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Add cardinality label
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    fig.add_annotation(
        x=mid_x, y=mid_y,
        text=cardinality,
        showarrow=False,
        bgcolor='white',
        bordercolor='#13343B',
        borderwidth=1,
        font=dict(size=10, color='#13343B')
    )

# Add entity boxes
for entity_name, entity_data in entities.items():
    x, y = entity_data['pos']
    attributes = entity_data['attributes']
    color = entity_data['color']
    
    # Create attribute text with proper formatting
    attr_text = f"<b>{entity_name}</b><br>"
    for attr in attributes:
        if '(PK)' in attr:
            attr_text += f"<b>🔑 {attr}</b><br>"
        elif '(FK)' in attr:
            attr_text += f"🔗 {attr}<br>"
        else:
            attr_text += f"• {attr}<br>"
    
    # Add entity as a scatter point with text
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode='markers+text',
        marker=dict(
            size=120,
            color=color,
            line=dict(width=2, color='#13343B')
        ),
        text=entity_name,
        textposition='middle center',
        textfont=dict(size=12, color='white'),
        hovertext=attr_text,
        hoverinfo='text',
        showlegend=False
    ))

# Update layout
fig.update_layout(
    title='Animal Adoption Database ERD',
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[-0.5, 2.5]
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[-0.5, 4.5]
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    annotations=[
        dict(
            text="Hover over entities to see attributes. PK=Primary Key, FK=Foreign Key",
            showarrow=False,
            xref="paper", yref="paper",
            x=0.5, y=-0.1,
            xanchor='center', yanchor='top',
            font=dict(size=12, color='#13343B')
        )
    ]
)

# Save the chart
fig.write_image('animal_adoption_erd.png')
fig.write_image('animal_adoption_erd.svg', format='svg')
print("Animal Adoption ERD created successfully!")