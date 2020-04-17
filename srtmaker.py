from timecode import Timecode
import time 

"""
Takes a text file formatted like: (last separator makes no difference)

00:00:00:00 - subtitle text
\n\n

and outputs a .srt subtitle formatted like

one-digit counter
TC in --> TC out
subtitle text
\n\n


output Timecode formatting is 00:00:00,00
"""
# open and read file
haiti = open('/Users/martimpassos/Downloads/haiti.txt', 'r', )
data = (haiti.read())

# list of subtitle entries (split text on blank newlines)
entries = data.split("\n\n")


counter = 1
final = ""

for entry in entries:

    entry_index = entries.index(entry)

    # find next entry TC in
    if entry_index < len(entries) - 1:
        next_entry = entries[entry_index+1]

    next_tc_in = Timecode('25', f"{next_entry.split(' - ')[0]}")

    # find current entry TC in
    tc_in = Timecode('25', f"{entry.split(' - ')[0]}")

    tc_in_str = str(Timecode('25', f"{entry.split(' - ')[0]}"))
    tc_in_str = tc_in_str[:8] + "," + tc_in_str[9:]

    # get current entry's text
    text = entry.split(" - ")[1]

    # determine subtitle duration based on character length
    duration = Timecode('25', f'00:00:{round(sum(len(characters) for characters in text.split()) * 0.17)};00')

    # generate TC out
    tc_out = (tc_in + duration)

    # make sure subtitles don't overlap
    one_frame = Timecode('25', '00:00:00:01')

    if tc_out.frames > next_tc_in.frames:
        tc_out = next_tc_in - one_frame

    tc_out_str = str(tc_out)
    tc_out_str = tc_out_str[:8] + "," + tc_out_str[9:]

    # format final string
    entry = f"{counter}\n{tc_in_str} --> {tc_out_str}\n{text}\n\n"

    counter += 1
    final += entry


#print(final)

# filename versioning
timestr = time.strftime("%H-%M-%S")

# write final string to file
haiti_fixed = open(f"/Users/martimpassos/Downloads/haiti-fixed_{timestr}.srt", "w")
haiti_fixed.write(final)
haiti_fixed.close()
