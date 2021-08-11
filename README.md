# RandomWolfGenerator
Randomly assigns roles to participants of the werewolf game, then sends them an email with their role.

For the emails to work you will need to configure your own SMTP server.
I am on Windows and I am using [hMailServer](https://www.hmailserver.com/download).

To disable email sends, open `configuration/email_config.ini` and set `send_email` to `0` (send_email,0).

To add players, insert them in `configuration/player_config.ini`.

Other packages:\
[termcolor](https://pypi.org/project/termcolor/) (pip install termcolor)