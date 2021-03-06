"""
Handles the new game configuration settings, etc.
"""

from functools import partial

from blaseball.util.qthelper import EasyDialog

from data import teamdata

class NewGame(EasyDialog):
    """The first dialog that greets users when the application is opened."""

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        for team in teamdata.TEAMS_99:
            team_fn = partial(self.main_window.load_game_and_ui.emit,
                              team + ": Day 1")
            self.add_button(team, team_fn)

        self.finish()