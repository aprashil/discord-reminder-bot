# Discord Reminder Bot

Discord Reminder Bot is a `discord.py` based event reminder.

## Packages 
1) [discord.py](https://pypi.org/project/discord.py/)
2) [os](https://docs.python.org/3/library/os.html)
3) [json](https://docs.python.org/3/library/json.html)

## Usage
- Install `discord.py` via the PIP package manager with the following command:
```bash
pip install discord.py
```
- Rename the _example.config.json_ and _example.events.json_ files to `config.json` and `events.json` respectively.

- Setup the configuration variables in _config.json_.

- Setup your events in _events.json_.

- Run index.py!

## FAQ:
1) How to obtain your [Bot Token](https://discordpy.readthedocs.io/en/latest/discord.html)?
2) How to obtain the [Channel ID](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)?

## Features:
- _events.json_ is reloaded every 30 seconds.

- The `tts` attribute in `config.json` stands for [_text-to-speech_](https://support.discord.com/hc/en-us/articles/212517297-Text-to-Speech-101), leaving it *True* would cause the bot to also send a second tts message in addition to the reminder embed message.

## Upcoming Features:
- Command based event/configuration setup.

## Contributing
Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)