Takes a text file formatted like: (second-frame separator makes no difference)

00:00:00:00 - subtitle text<br>
{newline}<br>
{newline}

and outputs a .srt subtitle formatted like

{one-digit counter}<br>
TC in --> TC out<br>
{subtitle text}<br>
{newline}<br>
{newline}


output Timecode formatting is 00:00:00,00 and subtitle duration is {character_count} * 0.17
