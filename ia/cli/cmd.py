"""cmd module.

Contains the different commands available.
"""

import sys
from pathlib import Path
from textwrap import wrap
from typing import Annotated, Optional, TextIO

import typer
from rich.console import Console
from rich.text import Text

from ia import __version__
from ia.graph import UndirectedGraph
from ia.graph.algorithm import TraversalAlgorithm
from ia.parser.graph.undirected import parse_and_transform


def run():
    """Configure and execute the CLI."""
    app = typer.Typer(pretty_exceptions_show_locals=False)
    app.command("uninformed")(uninformed)
    app.command("preview")(preview)
    app(prog_name="ia")


def version_callback(value: bool):
    """Print the version."""
    if value:
        print(f"ia version {__version__}")
        raise typer.Exit()


def uninformed(
    input_path: Annotated[
        Path,
        typer.Argument(
            help="The path to the file containing the graph.",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
        ),
    ],
    algorithm: Annotated[
        TraversalAlgorithm,
        typer.Option(
            help="Traversal algorithm to use.",
        ),
    ],
    start: Annotated[
        int,
        typer.Option(
            "--start",
            "-s",
            help="The starting vertex.",
        ),
    ],
    end: Annotated[
        int,
        typer.Option(
            "--end",
            "-e",
            help="The ending vertex.",
        ),
    ],
    output_path: Annotated[
        Optional[Path],
        typer.Option(
            "--output",
            "-o",
            help="The path to the file to write the output to.",
            writable=True,
            resolve_path=True,
        ),
    ] = None,
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            callback=version_callback,
            help="Print the program version.",
        ),
    ] = None,
    preview: Annotated[
        Optional[bool],
        typer.Option(
            "--preview",
            "-p",
            help="Render the generated tree.",
        ),
    ] = None,
):
    """Traverse the graph using the specified algorithm."""
    console = Console()
    graph = None
    with open(input_path) as input_file:
        graph = parse_and_transform(input_file.read())
        if graph is None:
            console.print("\nFailed to parse the graph.", style="red bold")
            raise typer.Exit(1)
    output_stream = sys.stdout if output_path is None else open(output_path, "w")
    print_result(graph, start, end, algorithm, file=output_stream)


def preview(
    input_path: Annotated[
        Path,
        typer.Argument(
            help="The path to the file containing the graph.",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
        ),
    ],
):
    """Render a graph preview."""
    console = Console()
    graph = None
    with open(input_path) as input_file:
        graph = parse_and_transform(input_file.read())
        if graph is None:
            console.print("\nFailed to parse the graph.", style="red bold")
            raise typer.Exit(1)
    import matplotlib.pyplot as plt
    import networkx as nx

    nx_graph = graph.to_networkx()
    plt.figure()
    plt.suptitle(f"Graph preview - {input_path.name}")
    plt.title("by @hadronomy")
    nx.draw_spring(nx_graph, with_labels=True, node_color="skyblue", node_size=500)
    plt.show()


def wrap_text(text, width):
    """Wrap text to a specified width.

    Parameters
    ----------
        text: str
            The text to wrap.
        width: str
            The width to wrap the text to.

    Returns
    -------
        str: The wrapped text.

    """
    return "\n".join(wrap(text, width=width))


def print_result(
    graph: UndirectedGraph,
    start: int,
    end: int,
    algorithm: TraversalAlgorithm,
    file: TextIO = sys.stdout,
):
    """Print the result of the traversal."""
    console = Console(file=file)
    width = 30
    divider = Text("-" * width, style="grey30")
    console.print(divider)
    console.print(f"Number of nodes: {len(graph.vertices())}", style="green bold")
    console.print(f"Number of edges: {len(graph.edges())}", style="green bold")
    console.print(f"Origin vertex: {start}", style="blue bold")
    console.print(f"Destination vertex: {end}", style="yellow bold")
    result = graph.traverse(start=start, end=end, algorithm=algorithm)
    for i, step in enumerate(result.history):
        console.print(divider)
        console.print(Text(f"Iteration {i + 1}", style="red bold"))
        console.print(
            wrap_text(
                f"Generated nodes: {", ".join(str(i) for i in step["generated"])}",
                width,
            )
        )
        console.print(
            wrap_text(
                f"Inspected nodes: {", ".join(str(i) for i in step["inspected"])}",
                width,
            )
        )
    console.print(divider)
    console.print(
        Text("Path:", style="bold"),
        wrap_text(
            f"{" -> ".join(str(i) for i in result.path)}",
            width - 3,
        ),
    )
    console.print(divider)
    console.print(Text("Cost:", style="bold"), f"{result.cost}")
    console.print(divider)
