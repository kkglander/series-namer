import typer
from typing import List
from typing_extensions import Annotated 

import os
from pathlib import Path
from natsort import natsorted

app = typer.Typer()

@app.command()
def cli(
        files: List[Path], 
        title: Annotated[str, typer.Option("--title", "-t", prompt="Enter the title of the show", help="Title of television show.")],
        season: Annotated[int, typer.Option("--season", "-s",help="Season of the television show")]= 1,
        episode: Annotated[int, typer.Option("--episode", "-e", help="The first episode that will be counted up from")]=1
):
    natsorted(files)
    for i in range(len(files)):
        file = files[i]
        if file.is_file():
            ext = file.suffix
            newName = f"{title} S{season:02d}E{episode + i:02d}"
            newFile = (file.parent / newName).with_suffix(ext)
            file.rename(newFile)
            print(f"{file} has been renamed to {newFile}.")
        else:
            print(f"{file} doesn't exist. :(")
        print("\n")

def main():
    app()


if __name__ == "__main__":
    app()
