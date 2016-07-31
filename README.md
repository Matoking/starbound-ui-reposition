# Starbound HUD Reposition
Starbound HUD Reposition is a game mod that allows HUD elements to be repositioned.

This is ideal for multi-monitor setups. If you have the game open on three monitors, you can reposition the HUD elements so that they only appear in the monitor in the middle.

# Installation (Linux)
The Python dependencies for this project are in the file 'requirements.txt'. Install them by running:

```
pip install -r requirements.txt
```

You should now be able to run *create_mod.py*, which creates the mod file.

You can also use the web application which has an easy-to-use interface for online users. The web application is built using Django; a local development server can be launched using the command

```
python manage.py runserver 8000
```

# Using the mod
Run the 'create_mod.py' to create the mod as a ZIP file. The script takes four parameters (top, right, bottom, left) which correspond to the amount of padding to the sides of the window resolution used by the game.

For example, if you have three 1080p (1920x1080) monitors and you want to place the HUD elements in the middle, you can use the following command to place the HUD in the middle monitor.

```
python create_mod.py 0 1920 0 1920
```

This will create a ZIP archive into the same directory containing the usable mod. Extract the created mod into Starbound's mods directory. If you have the game on Steam, the path could be the following:

```
STEAM_LIBRARY/common/Starbound/mods
```

If you have extracted the mod correctly, there should be a new directory *hud_reposition* inside. Just restart the game and the mod should work automatically.

# Limitations
Since the HUD elements can only be repositioned by loading a mod on startup, changing the resolution of the game will require the mod to be regenerated.

# License
Starbound HUD Reposition is licensed under the *CC0 1.0 Universal* public domain license.
