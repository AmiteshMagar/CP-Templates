import sublime
import sublime_plugin

def plugin_loaded():
    sublime.active_window().run_command('set_layout', {
    	"cols": [0.0, 0.70, 1.0], 
    	"rows": [0.0, 1.0]
    	"cells": [[0, 0, 1, 2], [1, 0, 2, 1],
    							[1, 1, 2, 2]]
 	})


# window.set_layout({
#     "cols": [0, 0.5, 1],
#     "rows": [0, 0.5, 1],
#     "cells": [[0, 0, 1, 2], [1, 0, 2, 1],
#                             [1, 1, 2, 2]]
# })