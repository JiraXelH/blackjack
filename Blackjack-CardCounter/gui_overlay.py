import PySimpleGUI as sg

# Initialize the window layout
layout = [
    [sg.Text('Detected Cards:', font=('Any', 12))],
    [sg.Text('', size=(40, 2), key='-CARDS-')],
    [sg.Text('Running Count:'), sg.Text('0', key='-RUN-')],
    [sg.Text('True Count:'), sg.Text('0', key='-TRUE-')],
]

# Create the window upfront so it can be updated from other modules
window = sg.Window(
    'Blackjack Card Counter',
    layout,
    keep_on_top=True,
    finalize=True,
)


def update_gui(cards, running_count, true_count):
    """Update the GUI elements with new values."""
    card_text = ', '.join(cards) if isinstance(cards, (list, tuple)) else str(cards)
    window['-CARDS-'].update(card_text)
    window['-RUN-'].update(str(running_count))
    window['-TRUE-'].update(str(true_count))
    window.refresh()


if __name__ == '__main__':
    try:
        while True:
            event, _ = window.read(timeout=100)
            if event == sg.WIN_CLOSED:
                break
    finally:
        window.close()
