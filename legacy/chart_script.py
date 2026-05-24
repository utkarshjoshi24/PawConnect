import plotly.graph_objects as go

# Create figure with more space
fig = go.Figure()

# Define layer positions with more spacing
layers = [
    {'name': 'Frontend Layer', 'y': 4.5, 'color': '#1FB8CD'},
    {'name': 'Web Server Layer', 'y': 3.2, 'color': '#DB4545'},
    {'name': 'Backend Layer', 'y': 1.9, 'color': '#2E8B57'},
    {'name': 'Database Layer', 'y': 0.6, 'color': '#5D878F'}
]

# Add layer background rectangles and labels
for layer in layers:
    # Layer background
    fig.add_shape(
        type="rect",
        x0=0, y0=layer['y']-0.5, x1=10, y1=layer['y']+0.5,
        fillcolor=layer['color'],
        opacity=0.1,
        line=dict(color=layer['color'], width=2)
    )
    
    # Layer title
    fig.add_annotation(
        x=0.2, y=layer['y']+0.3,
        text=f"<b>{layer['name']}</b>",
        showarrow=False,
        font=dict(size=16, color=layer['color']),
        xanchor="left"
    )

# Define components with better spacing
components = [
    # Frontend Layer
    {'name': 'HTML Pages', 'detail': 'index.html<br>animal.html<br>admin.html<br>adoption_form.html', 'x': 2.5, 'y': 4.5, 'color': '#1FB8CD'},
    {'name': 'CSS/JavaScript', 'detail': 'styles.css<br>Interactive Scripts', 'x': 6.5, 'y': 4.5, 'color': '#1FB8CD'},
    
    # Web Server Layer
    {'name': 'Web Server', 'detail': 'Apache/Nginx', 'x': 2.5, 'y': 3.2, 'color': '#DB4545'},
    {'name': 'CGI Interface', 'detail': 'Request Handler', 'x': 6.5, 'y': 3.2, 'color': '#DB4545'},
    
    # Backend Layer
    {'name': 'C Programs', 'detail': 'server.c, db.c, api.c<br>JSON Processing', 'x': 4.5, 'y': 1.9, 'color': '#2E8B57'},
    
    # Database Layer
    {'name': 'SQLite Database', 'detail': 'adoption.db', 'x': 3, 'y': 0.6, 'color': '#5D878F'},
    {'name': 'Database Tables', 'detail': 'Animals, Users<br>Adoptions, Admins', 'x': 6, 'y': 0.6, 'color': '#5D878F'}
]

# Add component boxes with better sizing
for comp in components:
    # Component box
    fig.add_shape(
        type="rect",
        x0=comp['x']-1, y0=comp['y']-0.3, 
        x1=comp['x']+1, y1=comp['y']+0.3,
        fillcolor=comp['color'],
        opacity=0.8,
        line=dict(color=comp['color'], width=2)
    )
    
    # Component name (larger text)
    fig.add_annotation(
        x=comp['x'], y=comp['y']+0.1,
        text=f"<b>{comp['name']}</b>",
        showarrow=False,
        font=dict(size=12, color='white'),
        xanchor="center"
    )
    
    # Component details (larger text)
    fig.add_annotation(
        x=comp['x'], y=comp['y']-0.1,
        text=comp['detail'],
        showarrow=False,
        font=dict(size=10, color='white'),
        xanchor="center"
    )

# Add cleaner flow arrows with better labels
flow_arrows = [
    # Frontend to Web Server
    {'start_x': 2.5, 'start_y': 4.2, 'end_x': 2.5, 'end_y': 3.5, 'label': 'HTTP Requests', 'label_x': 1.8, 'label_y': 3.85},
    
    # Web Server internal
    {'start_x': 3.5, 'start_y': 3.2, 'end_x': 5.5, 'end_y': 3.2, 'label': 'CGI Calls', 'label_x': 4.5, 'label_y': 3.4},
    
    # Web Server to Backend
    {'start_x': 6.5, 'start_y': 2.9, 'end_x': 4.8, 'end_y': 2.2, 'label': 'Execute Programs', 'label_x': 6, 'label_y': 2.55},
    
    # Backend to Database
    {'start_x': 4.2, 'start_y': 1.6, 'end_x': 3.3, 'end_y': 0.9, 'label': 'SQL Queries', 'label_x': 3.2, 'label_y': 1.25},
    
    # Return paths
    {'start_x': 3, 'start_y': 0.9, 'end_x': 4.2, 'end_y': 1.6, 'label': 'Query Results', 'label_x': 4, 'label_y': 1.25},
    {'start_x': 4.2, 'start_y': 2.2, 'end_x': 6.2, 'end_y': 2.9, 'label': 'JSON Response', 'label_x': 5, 'label_y': 2.55},
    {'start_x': 5.5, 'start_y': 3.2, 'end_x': 3.5, 'end_y': 3.2, 'label': 'HTTP Response', 'label_x': 4.5, 'label_y': 3.0},
    {'start_x': 2.5, 'start_y': 3.5, 'end_x': 2.5, 'end_y': 4.2, 'label': 'HTML/JSON Data', 'label_x': 3.2, 'label_y': 3.85}
]

# Add arrows with better visibility
for arrow in flow_arrows:
    # Add arrow
    fig.add_annotation(
        x=arrow['end_x'], y=arrow['end_y'],
        ax=arrow['start_x'], ay=arrow['start_y'],
        xref='x', yref='y', axref='x', ayref='y',
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=3,
        arrowcolor='#333333'
    )
    
    # Add label separately for better positioning
    fig.add_annotation(
        x=arrow['label_x'], y=arrow['label_y'],
        text=arrow['label'],
        showarrow=False,
        font=dict(size=10, color='#333333'),
        xanchor="center",
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor="#333333",
        borderwidth=1
    )

# Add database connection line
fig.add_shape(
    type="line",
    x0=3, y0=0.6, x1=6, y1=0.6,
    line=dict(color='#5D878F', width=3, dash='dash')
)

# Configure layout
fig.update_layout(
    title="Animal Adoption System Architecture",
    xaxis=dict(range=[-0.5, 10.5], showticklabels=False, showgrid=False, zeroline=False),
    yaxis=dict(range=[0, 5.2], showticklabels=False, showgrid=False, zeroline=False),
    plot_bgcolor='white',
    showlegend=False
)

# Save the chart
fig.write_image("architecture_diagram.png")
fig.write_image("architecture_diagram.svg", format="svg")
print("Updated architecture diagram saved as architecture_diagram.png and architecture_diagram.svg")