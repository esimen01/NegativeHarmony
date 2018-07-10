letters = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
accidentals = {'bb': -2, 'b': -1, '': 0, '#': 1, 'x': 2}
qualities = {'': [0, 4, 7], 'm': [0, 3, 7], '+': [0, 4, 8], 'o': [0, 3, 6],
             'M7': [0, 4, 7, 11], '7': [0, 4, 7, 10], 'm7': [0, 3, 7, 10],
             'ø': [0, 3, 6, 10]}

half_step_up = {'A': True, 'B': False, 'C': True, 'D': True, 'E': False, 
                'F': True, 'G': True}
half_step_dn = {'A': True, 'B': True, 'C': False, 'D': True, 'E': True, 
                'F': False, 'G': True}
accidentals = {'bb': -2, 'b': -1, '': 0, '#': 1, 'x': 2}
acc_rev = {-2: 'bb', -1: 'b', 0: '', 1: '#', 2: 'x'}
possible_notes = [['C', 'B#', 'Dbb'], ['C#', 'Db'], ['D', 'Cx', 'Ebb'],
                  ['Eb', 'D#', 'Fbb'], ['E', 'Dx', 'Fb'], ['F', 'E#', 'Gbb'],
                  ['F#', 'Gb', 'Ex'], ['G', 'Fx', 'Abb'], ['G#', 'Ab'],
                  ['A', 'Bbb', 'Gx'], ['Bb', 'A#', 'Cbb'], ['B', 'Ax', 'Cb']]

print("This is a Negative Harmony finder.")
print("It requires a chord, and an axis for reflection.")
print("Use 'b' for flats and '#' for sharps.")

axis_raw = input("Enter the desired axis (e.g., Bb/F): ")
axis = axis_raw.split("/")

for i in range(0, len(axis)):
    axis[i] = axis[i][0].upper() + axis[i][1:]
if len(axis) == 1:
    
    axis_2_letter = letters[(letters.index(axis[0][1]) + 5) % 7]
    for i in range(0, 12):
        if axis[0] in possible_notes[i]:
            root_num = i
            break
    axis.append(axis[0])

chord_raw = input("Enter the desired chord (e.g., Cm7): ")

root = ""
accidental = ""
quality = ""

if len(chord_raw) == 1:
    root = chord_raw.upper()
else:
    if chord_raw[1] == 'b' or chord_raw[1] == '#':
        root = chord_raw[0].upper()
        accidental = chord_raw[1]
        quality = chord_raw[2:]
    else:
        root = chord_raw[:1].upper()
        quality = chord_raw[1:]

root_num = -1

for i in range(0, 12):
    if root+accidental in possible_notes[i]:
        root_num = i
        break

letter_num = letters.index(root)

intervals = qualities[quality]
pitches = []

for i in range(0, len(intervals)):
    for pitch in possible_notes[(root_num + intervals[i]) % 12]:
        if letters[(letter_num + (2*i)) % 7] == pitch[:1]:
            pitches.append(pitch)
            break

print(pitches)

axis_num = []

for endpoint in axis:
    for pitch in possible_notes:
        if endpoint in pitch:
            axis_num.append(possible_notes.index(pitch))
            break

distances_from_axis = [pitch-axis_num[0]+root_num for pitch in intervals]

new_root_num = (axis_num[1] - distances_from_axis[0]) % 12
new_root = ""

letter_dist = (letters.index(root) - letters.index((axis[0])[:1])) % 7

for pitch in possible_notes[new_root_num]:
    if (letters.index((axis[1])[:1]) - letters.index(pitch[:1])) % 7 \
             == letter_dist:
        new_root = pitch

new_letter_num = letters.index(new_root[:1])

new_pitches = []

for i in range(0, len(intervals)):
    for pitch in possible_notes[(new_root_num - intervals[i]) % 12]:
        if letters[(new_letter_num - (2*i)) % 7] == pitch[:1]:
            new_pitches = [pitch] + new_pitches
            break

print(new_pitches)

new_intervals = [intervals[-1] - pitch for pitch in intervals]
new_intervals.reverse()

new_quality = ""
for quality in qualities:
    if qualities[quality] == new_intervals:
        new_quality = quality
        break

print(new_pitches[0] + new_quality)