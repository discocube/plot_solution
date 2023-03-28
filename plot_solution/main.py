import argparse
import pandas as pd
import plotly.express as px


def main():
    """
    Parses command line arguments and creates a 3D line plot from a CSV file.
    
    Command Line Arguments:
    -----------------------
    file_path : str
        The path to the CSV file containing the data to be plotted.
    """
    parser = argparse.ArgumentParser(description='Create a 3D line plot from a CSV file.')
    parser.add_argument('file_path', type=str, help='path to CSV file')
    args = parser.parse_args()

    create_3d_line_plot(args.file_path)


def create_3d_line_plot(file_path):
    """
    Reads a CSV file and creates a 3D line plot of the data.

    Parameters:
    -----------
    file_path : str
        The path to the CSV file containing the data to be plotted.

    Returns:
    --------
    None

    Raises:
    -------
    FileNotFoundError
        If the file specified by `file_path` does not exist.

    ValueError
        If the CSV file specified by `file_path` cannot be parsed by `pd.read_csv()`.
    """
    df = pd.read_csv(file_path)
    fig = px.line_3d(df, x='X', y='Y', z='Z')
    fig.show()


if __name__ == '__main__':
    main()