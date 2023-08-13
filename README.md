# Interactive Sales Dashboard with Streamlit

This repository contains an example of an interactive sales dashboard built using Streamlit. Streamlit is a Python library that enables you to create interactive web applications for data visualization without the need for HTML or CSS coding.

## Getting Started

To run this interactive sales dashboard locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/itskmyoo/ob-sample-streamlit.git 
   ```
2. Navigate to the project directory:

   ```bash
   cd ob-sample-streamlit
   ```
3. Install the required Python packages (you might want to use a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. A new browser tab will open with the interactive dashboard.

## About the Dashboard
This interactive sales dashboard allows you to explore sales data using various filters and visualize revenue trends. It demonstrates how to use Streamlit widgets, data filtering, and Matplotlib for data visualization.

## Example Data
The sample sales data used in this dashboard is generated programmatically. To generate your own sample data, you can refer to the provided generate_sample_data.py script. Run the script to create a CSV file named `sample_sales_data.csv`.

## Repository Structure
`app.py`: The Streamlit app script containing the interactive dashboard code.
`sample_sales_data.csv`: Sample sales data in CSV format.
`generate_sample_data.py`: Python script to generate sample sales data.
`requirements.txt`: List of Python packages required for this project.

## Author
This project was created by [@itskmyoo](https://github.com/itskmyoo)

## Contributions
Feel free to contribute to this project by opening issues or submitting pull requests. Your input is highly appreciated!

## License
This project is licensed under the MIT License

## Blog 

[Building Interactive Sales Dashboards with Streamlit: No HTML or CSS Hassles, Just Python Power](https://itskmyoo.medium.com/building-interactive-sales-dashboards-with-streamlit-no-html-or-css-hassles-just-python-power-d3347bdcb66b)