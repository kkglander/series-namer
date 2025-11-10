# rip-factory
Simple CLI for renaming media files so that they will be properly displayed on Jellyfin. You can input as many files as you want and it uses natural sort so it shouldn't mess episode order. Its useful for renaming entire show directories at once, but can also rename small file groups like the ones produced when ripping episodes with Makemkv. The episode flag makes it so that you can name the next group from where you left off.

#USAGE
rip-factory [OPTIONS] FILES...

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    files      FILES...  [required]                                                                                                                                                                           │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --title               -t      TEXT     Title of television show. [required]                                                                                                                                 │
│    --season              -s      INTEGER  Season of the television show [default: 1]                                                                                                                           │
│    --episode             -e      INTEGER  The first episode that will be counted up from [default: 1]                                                                                                          │
│    --help                                 Show this message and exit.                                                                                                                                          │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
