from abjad import *
import sys
MIDI_TO_LILYPOND = -58
AMPLITUDE_THRESHOLD = 80

def make_staff(pitches, durations):
    items = []
    for i in range(0, len(pitches)):
        if (pitches[i] == None):
            items.append(Rest(durations[i]))
        else:
            items.append(Note(pitches[i], durations[i]))
    staff = Staff(items)
    return staff

if len(sys.argv) < 2:
    print "Please specify a file name!"
    exit()

f = open(sys.argv[1], "r")
data = f.readlines()
print str(data)
subdivision = (int)(data[0])
readings_per_subdisivion = (int)(data[1])
print subdivision
print readings_per_subdisivion

pitches = []
durations = []
numNotes = 0
pitchSum = 0
previousDuration = None
for i in range(2, len(data)):
    tokens = data[i].strip().split(' ')
    pitch = int(round((float)(tokens[0])))
    amplitude = int(round((float)(tokens[1])))
    if (amplitude > AMPLITUDE_THRESHOLD):
        numNotes+=1
        pitchSum += pitch
    #Determine if i is in the last group of an average
    if (i - 2 + 1) % readings_per_subdisivion == 0:
        if (numNotes >= readings_per_subdisivion / 2 and numNotes != 0):
            pitch = pitchSum / numNotes + MIDI_TO_LILYPOND
        else:
            pitch = None
        if len(pitches) > 0 and pitches[len(pitches) - 1] == pitch:
            print previousDuration.numerator
            newDuration = Duration(previousDuration.numerator + subdivision / previousDuration.denominator, subdivision)
            if newDuration.is_assignable:
                durations[len(durations) - 1] = newDuration
                print pitch
                print durations[len(durations) -1]
            else:
                pitches.append(pitch)
                durations.append(Duration(1, subdivision))
        else:
            pitches.append(pitch)
            durations.append(Duration(1, subdivision))
        previousDuration = durations[len(durations) - 1]
        pitchSum = 0
        numNotes = 0
f.close()
print pitches
print durations

staff = make_staff(pitches, durations)
show(staff)
