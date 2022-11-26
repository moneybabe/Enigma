# Enigma

##### This project implements the enigma machine with python. <br />
Here is a link to a youtube video showing a physical engima and a brief intro to its mechanism: https://www.youtube.com/watch?v=ASfAPOiq_eQ <br />
Here is a link to a youtube video explaining its mechanism in detail with animation aid: https://www.youtube.com/watch?v=ybkkiGtJmkM <br />

## Components of the enigma machine
The enigma machines consists of three main components: 1) plugboard, 2) three rotors, 3) reflector. <br />

### Plugboard
There are 26 holes corresponding to 26 alphabet. <br />
Users can connect any two holes with a wire, up to 13 connects (because 26 alphabets). For example, connecting 'A' with 'F' will map the letter 'A' as 'F' after passing through the plugboard, and vice versa. <br />
During WWII, german military usually use up to 10 wires only, which will be imitated in our Enigma machine.

### Rotor
There are a total of 5 standard rotors. <br />
Each rotor has different pre-determined internal wirings that map each letter to another letter. <br />
Users have to choose 3 rotors out of 5 and arrange them in any order. Users also need to configure the inital rotational position of each rotor. <br />
After ciphering each letter, the first rotor will rotate by one slot. For every full rotation (shifted 26 slots) of the first rotor, the second rotor will rotate by one slot. For everyone full rotation of the second rotor, the third rotor will rotate by one slot. <br />

### Reflector
The reflector has pre-determined internal wirings that map each letter to another.

## Required machine configruations
There are three major configurations needed before operating the machine. <br />
- Plugboard wirings
- Rotors' order arrangment
- Rotors' initial rotational position

## Algorithm of the enigma machine
Assume all rotors are aligned (intial rotational positions of all rotors are 0): <br />
When the user presses a letter, <br /> 
1. the first rotor will rotate by one slot
2. the letter will be mapped by the plugboard [e.g. 'A' -> 'F']
3. enter the first rotor after shifting foward by one key (because the first rotor rotated by one slot) [e.g. 'F' -> 'G']
4. mapped by the internal wiring of first rotor [e.g. 'G' -> 'P']
5. enter the second rotor after shifting backward by one key (because the second rotor is one slot behind first rotor) [e.g. 'P' -> 'O']
6. mapped by the internal wiring of second rotor [e.g. 'O' -> 'J']
7. enter the third rotor without shifting (second and third rotor are aligned) [e.g. 'J' -> 'J']
8. mapped by the internal wiring of third rotor [e.g. 'J' -> 'K']
9. enter the reflector withou shifting (third rotor and reflector are aligned) [e.g. 'K' -> 'K']
10. mapped by the internal wiring of reflector [e.g. 'K' -> 'L']
11. exit reflector and reenter third rotor without shifting [e.g. 'L' -> 'L']
12. mapped by the internal wiring of third rotor [e.g. 'L' -> 'G']
13. exit third rotor and reenter second rotor without shifting [e.g. 'G' -> 'G']
14. mapped by the internal wiring of second rotor [e.g. 'G' -> 'E']
15. exit second rotor and reenter first rotor after shifting forward by one key [e.g. 'E' -> 'F']
16. mapped by the internal wiring of first rotor [e.g. 'F' -> 'Q']
17. exit first rotor and reenter plugboard after shifting backward by one key [e.g. 'Q' -> 'P']
18. mapped by the plugboard (assume 'P' is not connected by wires) [e.g. 'P' -> 'P']
19. light up the corresponding lightbulb 
- 'A' is mapped to 'P' ultimately

### Remark
Enigma is self-reciprocal because of the reflector. <br />
It means to decrypt the message, you need to configure the enigma machine the same way as the sender and input the cipher text, which will return the plain text.

## How to operate the python-coded Enigma
Execute `$python main.py`. <br />
Configure the enigma machine according to instructions and input the message. <br />

### Unit test
Execute `$pytest test_enigma.py`

### Credit
Credit to @mauricioaniche for providing the testing module: https://gist.github.com/mauricioaniche/671fb553a81df9e6b29434b7e6e53491
