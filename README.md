# ip-ports-for-ceh-game
## Simple python drag-and-drop game to help remember services and their ports.
## Description
The game contains most common ports and services that are expected during CEHv11 exam. By playing it one can solidify their association knowledge.


## Getting Started

Ensure requirements of Python and pip are satisfied then follow installation instructions.

### Dependencies
- Python 3.8.10+
- pip 20.0.2+
- requirements.txt

### Installing
Run below commands to download project and dependencies:
```
git clone https://github.com/MaxOfLondon/ip-ports-for-ceh-game.git
cd ip-ports-for-ceh-game
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Executing program
Run below command:
```
python pgports.py
```
## How to play

Click and drag port number from the left column towards correct service name on the right. If association is correct the port will change colour and lock in to position where it is dropped.
Once completed click Next button to randomnly select next batch.
Hoverig mouse over a service name displays some addtional information about the service. These can be edited in ports.py as needed.

Hint: Drop port close to the service name label because you won't be able to drag it again if association made was correct and it may obscure other port preventing from dragging it.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details