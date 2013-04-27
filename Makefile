UI_FILES= P2PDemoTabView.py FigureWidget.py p2pdemo_mainWindow.py

all: $(UI_FILES) icons_rc.py

%.py : %.ui
	pyuic4 -x -o $@ $<
icons_rc.py: icons.qrc
	pyrcc4 icons.qrc > icons_rc.py
