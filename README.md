# rip-factory
Simple CLI for renaming media files so that they will be properly displayed on Jellyfin. You can input as many files as you want and it uses natural sort so it shouldn't mess episode order. Its useful for renaming entire show directories at once, but can also rename small file groups like the ones produced when ripping episodes with Makemkv. The episode flag makes it so that you can name the next group from where you left off.

# HOW TO
```$ pip install https://github.com/kkglander/rip-factory/releases/download/v0.1.0-alpha/rip_factory-0.0.1.tar.gz```

# USAGE
rip-factory [OPTIONS] FILES...

### Arguments
   files&emsp;&emsp;FILES...&emsp;[required]
### Options   
  --title&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;-t&emsp;&emsp;&emsp;TEXT&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;Title of television show. [required]  
  --season&emsp;&emsp;&emsp;&nbsp;&nbsp;-s&emsp;&emsp;&emsp;INTEGER&emsp;&emsp;&emsp;Season of the television show [default: 1]  
  --episode&emsp;&emsp;&emsp;-e&emsp;&emsp;&emsp;INTEGER&emsp;&emsp;&emsp;The first episode that will be counted up from [default: 1]  
  --help &emsp;&emsp;&emsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Show this message and exit.  
