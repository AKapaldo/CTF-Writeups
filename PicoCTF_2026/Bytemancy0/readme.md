# 📦 Bytemancy 0

|Category         |	Author                |
|-----------------|-----------------------|
|📦 Miscellaneous        |LT 'syreal' Jones    |

## Challenge Prompt

Can you conjure the right bytes? The program's source code can be downloaded here.

Additional details will be available after launching your challenge instance.

## Problem Type
- Python

## Solve
We are given the program source code:
```python
while(True):
  try:
    print('⊹──────[ BYTEMANCY-0 ]──────⊹')
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print()
    print('Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.')
    print()
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print('⊹─────────────⟡─────────────⊹')
    user_input = input('==> ')
    if user_input == "\x65\x65\x65":
      print(open("./flag.txt", "r").read())
      break
    else:
      print("That wasn't it. I got: " + str(user_input))
      print()
      print()
      print()
  except Exception as e:
    print(e)
    break
```

So all we need to do is send this program \x65\x65\x65.<br>
In CyberChef we can see that is just `eee`.
<img width="797" height="216" alt="2026-03-10_19-57-54" src="https://github.com/user-attachments/assets/73ffdffb-0c20-4bea-a63b-97537ab045e0" />

So we can connect to the machine using `nc` and then send the box the 3 `e` characters in a row.
<img width="532" height="242" alt="2026-03-21_12-55-00" src="https://github.com/user-attachments/assets/c0b57d46-31f6-424f-bf4d-aa4e8608f9c7" />

When we do that, we are presented with the flag!

<p align="right">(<a href="#top">back to top</a>)</p>

