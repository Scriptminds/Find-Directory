import os
import subprocess
import nuke

# Function to open the directory of the selected node (if it contains a valid file path)
def open_node_directory():
    try:
        # Get the selected node
        selected_node = nuke.selectedNode()

        # Check if the node has a 'file' or similar attribute
        if 'file' in selected_node.knobs():
            # Get the file path from the node
            file_path = selected_node['file'].value()

            # Convert the file path to an absolute path
            file_path = os.path.abspath(file_path)

            # Get the directory path (without the file name)
            directory_path = os.path.dirname(file_path)

            # Open the directory in Windows Explorer
            subprocess.Popen(f'explorer \"{directory_path}\"')
        else:
            nuke.message("Selected node doesn't contain a 'file' attribute.")
    except Exception as e:
        nuke.message(f"Error: {e}")

