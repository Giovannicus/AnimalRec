from IPython.display import display, HTML

def logo():
    html_content = """
    <div style="background-color: none; width: 300px; height: 300px; display: flex; justify-content: center; align-items: center; margin: 50px auto;">
        <div style="width: 220px; height: 220px; position: relative">
            <div class="image-container">
                <img src="traffic_sign.png">
            </div>
                <div class="circular-text" style="animation: spin 30s linear infinite; width: 100%; height: 100%; position: absolute; top: 0; left: 0;">
                    <style>
                        @keyframes spin {
                            0% { transform: rotate(0deg); }
                            100% { transform: rotate(360deg); }
                        }
                        .circular-text {
                            position: absolute;
                            top: 50%;
                            left: 50%;
                            width: 100%;
                            height: 100%;
                            transform: translate(100%, 100%);
                        }
                        .circular-text span {
                            position: absolute;
                            top: 50%;
                            left: 50%;
                            font-size: 20px;
                            color: white;
                            text-shadow: 1px 1px 0 red, -1px -1px 0 red, 1px -1px 0 red, -1px 1px 0 red;
                            transform-origin: 0 0;
                            transform: rotate(calc(var(--i) * 1deg)) translateY({100}px);                   
                        }
                    </style>
            """

    text = "Autonomous Vehicles Animal Detection "
    for i, char in enumerate(text):
        angle = i * 360 / len(text)
        html_content += f"""
            <span style="position: absolute; top: 50%; left: 50%; font-size: 30px; color: white; 
                        transform: rotate({angle}deg) translateY(-180px);
                        writing-mode: vertical-rl; text-orientation: upright;">
                {char}
            </span>
        """

    html_content += """
        </div>
    </div>
    """

    display(HTML(html_content))