autoscribe
==========

A set of utilities to transcribe audio--that is, produce sheet music from audio.

Tools Needed
===========
* pd-extended
* Python 2.7
* Lilypond
* Abjad: http://abjad.mbrsi.org/ 

Usage
=====
* Use Pure Data to run audio-to-text.pd. Choose tempo, subdivision, and number of subdivisions where labeled. Press the "start" bang, input audio, then press the "stop" message when done.
* Move the generated file from /tmp over to the directory with this program. Run `python interpreter.py [FILENAME]` to get sheet music.

Status
======
It is not perfect at transcribing at the moment, but can depict the general idea of the notes it is given. I will work on making it more accurate (and encourage anyone with ideas to make it more accurate to submit issues/pull requests).
