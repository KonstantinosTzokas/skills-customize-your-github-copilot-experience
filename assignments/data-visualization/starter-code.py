"""
Python Data Visualization Starter Code

This starter template provides a framework for creating visualizations
with matplotlib and plotly. Complete the implementation by adding functions
to create various charts and customize them effectively.
"""

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from typing import List, Dict, Tuple, Any


# ============================================================================
# TASK 1: Creating Charts with Matplotlib
# ============================================================================

def create_line_plot(x_data: List[float], y_data: List[float], 
                     title: str = "Line Plot", xlabel: str = "X", 
                     ylabel: str = "Y") -> None:
    """
    Create and display a line plot using matplotlib.
    
    Args:
        x_data: X-axis values
        y_data: Y-axis values
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
    """
    # TODO: Create line plot with matplotlib
    # - Plot the data with appropriate line style
    # - Add title, axis labels, and grid
    # - Display the plot
    pass


def create_bar_chart(categories: List[str], values: List[float],
                     title: str = "Bar Chart", xlabel: str = "Category",
                     ylabel: str = "Value") -> None:
    """
    Create and display a bar chart using matplotlib.
    
    Args:
        categories: List of category names
        values: List of corresponding values
        title: Chart title
        xlabel: X-axis label
        ylabel: Y-axis label
    """
    # TODO: Create bar chart
    # - Create bars for each category
    # - Customize colors for visual appeal
    # - Add labels and title
    # - Display the chart
    pass


def create_histogram(data: List[float], bins: int = 10,
                     title: str = "Histogram", xlabel: str = "Value",
                     ylabel: str = "Frequency") -> None:
    """
    Create and display a histogram using matplotlib.
    
    Args:
        data: List of data values
        bins: Number of histogram bins
        title: Histogram title
        xlabel: X-axis label
        ylabel: Y-axis label
    """
    # TODO: Create histogram
    # - Generate histogram with appropriate number of bins
    # - Add title and axis labels
    # - Customize appearance
    # - Display the histogram
    pass


def create_scatter_plot(x_data: List[float], y_data: List[float],
                        title: str = "Scatter Plot", xlabel: str = "X",
                        ylabel: str = "Y", sizes: List[float] = None,
                        colors: List[str] = None) -> None:
    """
    Create and display a scatter plot using matplotlib.
    
    Args:
        x_data: X-axis values
        y_data: Y-axis values
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        sizes: Optional list of point sizes
        colors: Optional list of point colors
    """
    # TODO: Create scatter plot
    # - Plot scatter points with customizable sizes and colors
    # - Add title and axis labels
    # - Include a legend if colors are provided
    # - Display the plot
    pass


def create_subplot_grid(plots_data: List[Dict[str, Any]]) -> None:
    """
    Create a grid of subplots with multiple visualizations.
    
    Args:
        plots_data: List of dictionaries containing plot specifications
                   Each dict should have: type, x_data, y_data, title, etc.
    """
    # TODO: Create subplot grid
    # - Determine grid size based on number of plots
    # - Create subplots
    # - Populate each subplot with appropriate visualization
    # - Add titles and labels to each subplot
    # - Display the figure
    pass


def save_plot(filename: str, format: str = 'png') -> None:
    """
    Save current plot to a file.
    
    Args:
        filename: Output filename (without extension)
        format: File format ('png', 'jpg', 'pdf', 'svg')
    """
    # TODO: Save the current figure
    # - Determine full filename with extension
    # - Save plot in specified format
    # - Use high DPI for quality
    pass


# ============================================================================
# TASK 2: Advanced Visualizations with Plotly
# ============================================================================

def create_interactive_bar_chart(categories: List[str], values: List[float],
                                 title: str = "Interactive Bar Chart") -> go.Figure:
    """
    Create an interactive bar chart using plotly.
    
    Args:
        categories: List of category names
        values: List of corresponding values
        title: Chart title
    
    Returns:
        Plotly figure object
    """
    # TODO: Create interactive bar chart
    # - Use plotly to create bar chart
    # - Add hover text with values
    # - Customize colors and styling
    # - Return the figure
    pass


def create_interactive_line_chart(x_data: List[float], y_data: List[float],
                                  title: str = "Interactive Line Chart") -> go.Figure:
    """
    Create an interactive line chart using plotly.
    
    Args:
        x_data: X-axis values
        y_data: Y-axis values
        title: Chart title
    
    Returns:
        Plotly figure object
    """
    # TODO: Create interactive line chart
    # - Plot line with hover information
    # - Add zoom and pan controls
    # - Customize styling
    # - Return the figure
    pass


def create_interactive_scatter_plot(x_data: List[float], y_data: List[float],
                                    labels: List[str] = None,
                                    title: str = "Interactive Scatter Plot") -> go.Figure:
    """
    Create an interactive scatter plot using plotly.
    
    Args:
        x_data: X-axis values
        y_data: Y-axis values
        labels: Optional labels for each point
        title: Chart title
    
    Returns:
        Plotly figure object
    """
    # TODO: Create interactive scatter plot
    # - Create scatter plot with point hover information
    # - Include labels in hover text if provided
    # - Customize colors and sizes
    # - Return the figure
    pass


def create_dashboard(data_dict: Dict[str, Dict[str, Any]]) -> go.Figure:
    """
    Create a dashboard combining multiple visualizations.
    
    Args:
        data_dict: Dictionary with subplot data
                  Keys: subplot titles
                  Values: dicts with 'type', 'x', 'y', etc.
    
    Returns:
        Plotly figure object with multiple subplots
    """
    # TODO: Create dashboard
    # - Create subplots from Plotly
    # - Add appropriate visualization for each subplot
    # - Configure layout and styling
    # - Return the figure
    pass


def save_interactive_plot(fig: go.Figure, filename: str) -> None:
    """
    Save interactive plotly figure to HTML file.
    
    Args:
        fig: Plotly figure object
        filename: Output filename (with .html extension)
    """
    # TODO: Save figure
    # - Save figure as interactive HTML
    # - Include all interactive features
    pass


# ============================================================================
# TASK 3: Data Visualization Best Practices
# ============================================================================

def choose_chart_type(data_description: str) -> str:
    """
    Recommend appropriate chart type for given data.
    
    Args:
        data_description: Description of the data and purpose
    
    Returns:
        Recommended chart type name
    """
    # TODO: Implement recommendation logic
    # - Analyze data description
    # - Return appropriate chart type (line, bar, scatter, etc.)
    pass


def create_colorblind_friendly_plot(x_data: List[float], y_data: List[float],
                                    title: str = "Colorblind-Friendly Plot") -> None:
    """
    Create a plot using colorblind-friendly color palette.
    
    Args:
        x_data: X-axis values
        y_data: Y-axis values
        title: Plot title
    """
    # TODO: Create plot with accessible colors
    # - Use colorblind-friendly palette
    # - Optionally add patterns or markers for distinction
    # - Document color choices
    pass


def compare_visualizations(data: List[float], title_prefix: str = "Data") -> None:
    """
    Create multiple visualizations of same data for comparison.
    
    Args:
        data: Input data to visualize
        title_prefix: Prefix for plot titles
    """
    # TODO: Create multiple visualizations
    # - Show data as histogram
    # - Show data as box plot
    # - Show data as KDE plot
    # - Compare their effectiveness in showing distribution
    pass


def annotate_plot_with_insights(x_data: List[float], y_data: List[float],
                                insights: List[Dict[str, Any]],
                                title: str = "Annotated Plot") -> None:
    """
    Create plot with annotations highlighting key insights.
    
    Args:
        x_data: X-axis values
        y_data: Y-axis values
        insights: List of insight dicts with 'x', 'y', 'label' keys
        title: Plot title
    """
    # TODO: Create annotated plot
    # - Plot data
    # - Add annotations for key insights
    # - Use arrows and text boxes for clarity
    # - Highlight important data points
    pass


# ============================================================================
# Main Program
# ============================================================================

if __name__ == "__main__":
    # Sample data for testing
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [100, 120, 115, 140, 155, 160]
    
    print("Python Data Visualization Assignment")
    print("=" * 50)
    
    # TODO: Add test cases for your implementations
