"""cmd module.

Contains the different commands available.
"""

import sys
from pathlib import Path
from textwrap import wrap
from typing import Annotated, TextIO

import typer
from rich.console import Console
from rich.text import Text

from ia import __version__
from ia.graph import UndirectedGraph
from ia.graph.algorithm import TraversalAlgorithm, TraversalResult
from ia.graph.parser import parse_and_transform
from ia.maze.maze import Maze
from ia.tree.utils import print_tree


def run():
    """Configure and execute the CLI."""
    app = typer.Typer(pretty_exceptions_show_locals=False)
    app.command("uninformed")(uninformed)
    app.command("informed")(informed)
    # This callback is needed to force typer to use
    # subcommands even when there is only one command.
    app.callback()(lambda: None)

    try:
        import matplotlib.pyplot as plt  # type: ignore # noqa: F401
        import networkx as nx  # type: ignore # noqa: F401

        app.command("preview")(preview)
    except ImportError:
        pass
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
        Path | None,
        typer.Option(
            "--output",
            "-o",
            help="The path to the file to write the output to.",
            writable=True,
            resolve_path=True,
        ),
    ] = None,
    version: Annotated[
        bool | None,
        typer.Option(
            "--version",
            "-v",
            callback=version_callback,
            help="Print the program version.",
        ),
    ] = None,
    preview: Annotated[
        bool | None,
        typer.Option(
            "--preview",
            "-p",
            help="Render the generated tree.",
        ),
    ] = None,
    force: Annotated[
        bool | None,
        typer.Option(
            "--force",
            "-f",
            help="Force the execution of the command.",
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

    if start not in graph.vertices:
        console.print(f"\nStart vertex {start} not in the graph.", style="red bold")
        if force:
            console.print(
                "Cannot force execution with invalid start node.", style="yellow bold"
            )
        raise typer.Exit(1)
    if end not in graph.vertices:
        console.print(f"\nEnd vertex {end} not in the graph.", style="red bold")
        if not force:
            raise typer.Exit(1)
        console.print("Forcing execution with invalid end node.", style="yellow bold")

    result = graph.traverse(start=start, end=end, algorithm=algorithm)
    print_result(graph, start, end, algorithm, result, file=output_stream)
    if preview:
        print_tree(result.tree)


def informed():
    """Traverse a maze using an informed search algorithm."""
    console = Console()
    maze = Maze(rows=10, cols=10)
    console.print(maze)
    console.print("\nMaze traversal not implemented yet.", style="red bold")
    console.print("\nInformed search not implemented yet.", style="red bold")
    raise typer.Exit(1)


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
    import matplotlib.pyplot as plt  # type: ignore
    import networkx as nx  # type: ignore

    nx_graph = graph.to_networkx()

    pos = nx.nx_agraph.graphviz_layout(nx_graph, prog="dot")

    plt.figure(figsize=(10, 10))
    plt.suptitle("Graph preview\nby @hadronomy")
    plt.title(f"{input_path.name}")
    plt.axis("off")
    plt.tight_layout()

    nx.draw_networkx_nodes(
        nx_graph, pos, node_color="white", edgecolors="black", node_size=700
    )
    nx.draw_networkx_edges(nx_graph, pos, edge_color="black", width=5)
    nx.draw_networkx_labels(nx_graph, pos, font_size=15, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(nx_graph, "weight")
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels)

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
    result: TraversalResult,
    file: TextIO = sys.stdout,
):
    """Print the result of the traversal."""
    console = Console(file=file)
    width = 35
    divider = Text("-" * width, style="grey30")
    console.print(divider)
    console.print(f"Number of nodes: {len(graph.vertices)}", style="green bold")
    console.print(f"Number of edges: {len(graph.edges)}", style="green bold")
    console.print(f"Origin vertex: {start}", style="blue bold")
    console.print(f"Destination vertex: {end}", style="yellow bold")
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
            width - 5,
        ),
    )
    console.print(divider)
    console.print(Text("Cost:", style="bold"), f"{result.cost}")
    console.print(divider)
