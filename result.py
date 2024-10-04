import plotly.graph_objects as go
import numpy as np

def plot_result(hist):
    epochs = np.arange(1, len(hist["loss"]) + 1)
    metrics = ["loss", "accuracy", "precision"]

    fig = go.Figure()

    for metric in metrics:
        fig.add_trace(go.Scatter(x=epochs, y=hist[metric], mode='lines',
                                 name=f'Training {metric}',
                                 line=dict(color='blue'),
                                 visible=(metric == "loss")))
        fig.add_trace(go.Scatter(x=epochs, y=hist[f'val_{metric}'], mode='lines',
                                 name=f'Validation {metric}',
                                 line=dict(color='orange'),
                                 visible=(metric == "loss")))

    dropdown_menu = []
    for i, metric in enumerate(metrics):
        dropdown_menu.append(dict(
            args=[{'visible': [False] * len(metrics) * 2},
                  {'title': f'{metric.capitalize()} over Epochs',
                   'yaxis': {'title': metric.capitalize()}}],
            label=metric.capitalize(),
            method='update'
        ))
        dropdown_menu[i]['args'][0]['visible'][i*2] = True  # Training metric
        dropdown_menu[i]['args'][0]['visible'][i*2+1] = True  # Validation metric

    fig.update_layout(
        updatemenus=[dict(
            active=0,
            buttons=dropdown_menu,
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,  # Moved down slightly
            yanchor="top"
        )],
        title="Model Training Metrics",
        xaxis_title="Epochs",
        yaxis_title="Loss",
        height=600,
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='black',
        showline=True,  # Show x-axis line
        linewidth=2,
        linecolor='black',
        dtick=1  # Set tick interval to 1
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='black',
        showline=True,  # Show y-axis line
        linewidth=2,
        linecolor='black'
    )

    fig.show()