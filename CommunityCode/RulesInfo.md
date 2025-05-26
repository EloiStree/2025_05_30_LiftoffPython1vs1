

You must run Telemetry Relay and XOMI on two mini-pc.
LiftOff send to the port 9001 the info of your game.
With Python Telemetry relay you diffuse your information to the other mini pc and other computer like osbserver and referee on the port 9002
XOMI allows to simulat the XBOX on the mini PC. from the port 3615.

The referee must know the ip of the two mini PC to reset the position of the drone and start the game.


For the POC sake:
- you are 1 vs 1
- one target is given

If Unity server on:
- Attacker is near target
  - One point to the attacker and full reset
- Defender is near attacker
  - One point to the defender and full reset
- In the first 20* seconds;
  - Defender must go at 50* meters of the target
  - Attcker must go out of 300* meters of the target

