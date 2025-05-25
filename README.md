Here is the corrected spelling and some minor grammatical improvements for your text:

---

# Liftoff Python 1v1

We would like to train a Python AI to fight 1v1 with the physics of Liftoff, defender vs attacker.

Listen to Liftoff telemetry:
[Liftoff Telemetry](https://github.com/EloiStree/2025_04_26_LiftoffTelemetryPyUnity/blob/main/README.md)

Remote control the drone:
[XOMI](https://github.com/EloiStree/2022_01_24_XOMI.git)

Push commands to the XOMI app to control the drone:
[UDP Gamepad to Liftoff](https://github.com/EloiStree/2025_04_26_UdpGamepadToLiftoffPyUnity.git)

You will need the two codes, which I have stored here in my case.
You can download the Zip of the executable or build the UDP.

```shell
mkdir "C:\Git\liftoff\"
cd "C:\Git\liftoff\"
git clone https://github.com/EloiStree/2025_04_26_LiftoffTelemetryPyUnity.git
git clone https://github.com/EloiStree/2025_04_26_UdpGamepadToLiftoffPyUnity.git
git clone https://github.com/EloiStree/2022_01_24_XOMI.git
```

In `shell:startup`

For the defender computer:

```shell
LaunchWidthDefenderIndexAbsolutePath.bat
python "C:\Git\liftoff\2025_04_26_LiftoffTelemetryPyUnity\Py\LiftOffPlayerIndexTelemetryRelay.py" 1
pause 15
```

For the attacking computer:

```shell
LaunchWidthAttackerIndexAbsolutePath.bat
python "C:\Git\liftoff\2025_04_26_LiftoffTelemetryPyUnity\Py\LiftOffPlayerIndexTelemetryRelay.py" 2
pause 15
```

For both computers:

```shell
LaunchGamepadSimulatorXOMI.bat
cd "C:\Git\liftoff\2022_01_24_XOMI\"
start "" "C:\Git\liftoff\2022_01_24_XOMI\bin\Debug\net9.0\XOMI.exe"
```


