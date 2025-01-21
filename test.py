import pyautogui
import time
from pynput import keyboard
from threading import Event, Thread
import sys
import pandas as pd

csv_file_path = 'results.csv'  # Replace with your actual file path

# Event to signal when to stop the script
stop_event = Event()

def on_press(key):
    """Callback function that gets called on key press."""
    if key == keyboard.Key.esc:
        print("Escape key pressed. Stopping script.")
        stop_event.set()  # Set the stop event to stop the script

def monitor_keyboard():
    """Function to start monitoring keyboard events."""
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def press_enter_double():
    """Function to press Enter key twice."""
    pyautogui.press('enter')
    pyautogui.press('enter')

def type_text(text):
    """Function to type text with a specific interval."""
    pyautogui.typewrite(text, interval=0.02)

def get_filtered_table(csv_file_path, specific_dates):
    """
    Reads a CSV file, filters the DataFrame by specific dates, and returns the filtered DataFrame.

    Parameters:
    csv_file_path (str): The path to the CSV file.
    specific_dates (list): A list of dates to filter the DataFrame.

    Returns:
    pd.DataFrame: A DataFrame containing only the rows that match the specified dates.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Select the columns in the desired order
    selected_columns = [
        'Date', 'UTS', 'YS', 'EL', 'Unit Weight', 'Transvers Height', 
        'Longitudinal Height', 'Rib spacing', 'Length', 'Bundle No'
    ]

    # Create a new DataFrame with the selected columns
    new_table = df[selected_columns].dropna()

    # Filter the DataFrame for the specific dates
    filtered_table = new_table[new_table['Date'].isin(specific_dates)]

    return filtered_table

def filter_by_bundle(filtered_data, starting_bundle):
    """
    Filters the DataFrame to include only rows from the specified starting bundle number.

    Parameters:
    filtered_data (pd.DataFrame): The DataFrame to filter.
    starting_bundle (int): The starting bundle number.

    Returns:
    pd.DataFrame: A DataFrame containing only the rows from the specified starting bundle.
    """
    return filtered_data[filtered_data['Bundle No'].astype(int) >= starting_bundle]


if __name__ == "__main__":
    # Start the keyboard monitoring thread
    keyboard_thread = Thread(target=monitor_keyboard)
    keyboard_thread.start()
    
    # Request date input from the user
    date_input = input("Please enter the date (format YYYY-MM-DD): ").strip()

    # Call the filtered table from the csv
    filtered_data = get_filtered_table(csv_file_path, [date_input])

    # Print the bundle numbers for user reference
    print("Available Bundle Numbers:")
    for bundle in filtered_data['Bundle No'].unique():
        print(bundle.astype(int))

   #for row_index in range(filtered_data.shape[0]):
        #print(filtered_data.iloc[row_index, 9].astype(int).astype(str))

    # Request starting bundle number from the user
    starting_bundle = int(input("Please enter the starting bundle number: ").strip())

    # Filter the data by the starting bundle number
    filtered_data = filter_by_bundle(filtered_data, starting_bundle)
    print(filtered_data)
    print(filtered_data.shape[0])
    # Wait for 5 seconds to switch to the right window
    time.sleep(5)

    # Iterate through each row and print the value in the second column (index 1)
    for row_index in range(filtered_data.shape[0]):    # Iterate over rows        
        if stop_event.is_set():
            break  # Exit the loop if the stop event is set
        try:
            # Extract values from the DataFrame
            uts_value = filtered_data.iloc[row_index, 1].astype(int)   # Get the UTS value from the second column
            ys_value = filtered_data.iloc[row_index, 2].astype(int)    # Get the YS value from the third column
            el_value = filtered_data.iloc[row_index, 3]    # Get the EL value from the forth column
            weight_value = filtered_data.iloc[row_index, 4]    # Get the Unit weight value from the fifth column
            t_height_value = filtered_data.iloc[row_index, 5]  # Get the Transverse Height value from the sixth column
            l_height_value = filtered_data.iloc[row_index, 6]  # Get the Longitudinal Height value from the seventh column
            rib_space_value = filtered_data.iloc[row_index, 7] # Get the Rib Spacing value from the eigth column
            length_value = filtered_data.iloc[row_index, 8].astype(int)    # Get the Length value from the nineth column
            print(uts_value)

            # Perform actions with optimized delays
            type_text(uts_value)
            pyautogui.press('enter')
            time.sleep(0.3)

            type_text(ys_value)
            press_enter_double()
            time.sleep(0.3)

            type_text(el_value)
            pyautogui.press('enter')
            time.sleep(0.3)

            type_text(weight_value)
            pyautogui.press('enter')
            time.sleep(0.3)

            type_text(t_height_value)
            pyautogui.press('enter')
            time.sleep(0.3)

            type_text(l_height_value)
            pyautogui.press('enter')
            time.sleep(0.3)

            type_text(rib_space_value)
            pyautogui.press('enter')
            time.sleep(0.3)

            type_text(length_value)
            pyautogui.press('enter')
            time.sleep(0.3)

            for i in range(4):
                type_text('ok')
                pyautogui.press('enter')
                time.sleep(0.3)
            
            pyautogui.click(x=62, y=337)
            time.sleep(0.3)
            pyautogui.click(x=210, y=337)
            time.sleep(0.3)

            for i in range(13):
                pyautogui.press('enter')
                time.sleep(0.4)

            #pyautogui.hotkey('ctrl', 's')
            time.sleep(100.5)
        except Exception as e:
            print(f"An error occurred: {e}")
            stop_event.set()  # Ensure the stop event is set in case of errors

    # Ensure the keyboard thread is properly closed
    keyboard_thread.join()
    print("Script terminated successfully.")
