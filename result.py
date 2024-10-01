import plotly.graph_objects as go
import numpy as np

def plot_res(n_epochs):

    epochs = np.arange(1, n_epochs)
    loss = np.random.uniform(0.2, 1.0, size=len(epochs))  # Loss simulata
    accuracy = np.random.uniform(0.5, 1.0, size=len(epochs))  # Accuracy simulata
    val_loss = np.random.uniform(0.3, 1.1, size=len(epochs))  # Val_loss simulata
    val_accuracy = np.random.uniform(0.4, 1.0, size=len(epochs))  # Val_accuracy simulata

    # Crea una figura Plotly
    fig = go.Figure()

    # Aggiungi i tracciati per ogni metrica
    fig.add_trace(go.Scatter(x=epochs, y=loss, mode='lines', name='Loss', visible=True))
    fig.add_trace(go.Scatter(x=epochs, y=accuracy, mode='lines', name='Accuracy', visible=False))
    fig.add_trace(go.Scatter(x=epochs, y=val_loss, mode='lines', name='Val Loss', visible=False))
    fig.add_trace(go.Scatter(x=epochs, y=val_accuracy, mode='lines', name='Val Accuracy', visible=False))

    # Definisci il menu a tendina per cambiare la metrica visualizzata
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(label="Loss",
                        method="update",
                        args=[{"visible": [True, False, False, False]},
                            {"title": "Training Loss"}]),
                    dict(label="Accuracy",
                        method="update",
                        args=[{"visible": [False, True, False, False]},
                            {"title": "Training Accuracy"}]),
                    dict(label="Val Loss",
                        method="update",
                        args=[{"visible": [False, False, True, False]},
                            {"title": "Validation Loss"}]),
                    dict(label="Val Accuracy",
                        method="update",
                        args=[{"visible": [False, False, False, True]},
                            {"title": "Validation Accuracy"}])
                ]),
                direction="down",  # Direzione del menu
                showactive=True  # Mostra il pulsante selezionato
            )
        ]
    )

    # Aggiungi titolo e etichette agli assi
    fig.update_layout(
        title="Metriche di Addestramento del Modello",
        xaxis_title="Epoche",
        yaxis_title="Valore",
        template="plotly_dark"  # Tema grafico
    )

    # Mostra il grafico
    fig.show()
