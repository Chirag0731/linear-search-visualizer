import gradio as gr

# ---------------------------------------------------------
# LINEAR SEARCH ALGORITHM (WITH STEP RECORDING)
# ---------------------------------------------------------
def linear_search(arr, target):
    """
    Perform a linear search on the list 'arr'.
    Returns a formatted string describing each step.
    """

    steps = []  # List to store text for each step of the algorithm

    for i in range(len(arr)):
        # Log each comparison
        steps.append(f"Step {i+1}: Checking index {i} → value {arr[i]}")

        # Check if the current value matches the target
        if arr[i] == target:
            steps.append(f"\n✅ FOUND {target} at index {i}")
            return "\n".join(steps)

    # If the loop ends with no match:
    steps.append(f"\n❌ {target} was NOT found in the list.")
    return "\n".join(steps)


# ---------------------------------------------------------
# INPUT PROCESSING FUNCTION
# ---------------------------------------------------------
def run_search(list_input, target_input):
    """
    Converts user input into integers,
    handles bad input, and runs linear_search().
    """

    try:
        # Convert space-separated input into a list of integers
        arr = list(map(int, list_input.split()))

        # Convert target input into an integer
        target = int(target_input)

        return linear_search(arr, target)

    except ValueError:
        # Error message shown if input is invalid
        return "⚠️ Invalid input! Please enter numbers separated by spaces and a valid target number."


# ---------------------------------------------------------
# USER INTERFACE (GRADIO)
# Works both locally and on Hugging Face Spaces
# ---------------------------------------------------------
with gr.Blocks() as demo:

    # Title
    gr.Markdown("<h1 style='color:#e63946; text-align:center;'>Linear Search Visualizer</h1>")

    # Subtitle
    gr.Markdown(
        "<p style='text-align:center; color:white;'>"
        "A clean, minimal red & black themed visualizer for the Linear Search algorithm."
        "</p>"
    )

    # Input fields
    with gr.Row():
        list_input = gr.Textbox(
            label="Enter numbers (space-separated)",
            placeholder="Example: 4 1 7 9 2"
        )
        target_input = gr.Textbox(
            label="Target number",
            placeholder="Example: 7"
        )

    # Output area
    output = gr.Textbox(
        label="Search Steps",
        lines=14
    )

    # Button
    run_btn = gr.Button("Run Search")

    # Connect button -> function -> output
    run_btn.click(run_search, inputs=[list_input, target_input], outputs=output)


# ---------------------------------------------------------
# LAUNCH APP
# ---------------------------------------------------------
demo.launch()

