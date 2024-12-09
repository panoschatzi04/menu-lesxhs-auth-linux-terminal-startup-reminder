# menu-lesxhs-auth-linux-terminal-startup-reminder
Πάντα ξεχνάω πότε είναι ανοιχτή η λέσχη και τι φαγητό έχει και έχω κουραστεί να ψάχνω κάθε φορά την σελίδα...

## Requirements

- Python 3.x
- Pandas library
- Datetime library
- Your custom Menu-Lesxhs Excel file. Mine is on the repo under the name `menu-lesxhs.xlsx`.

By default the plugin is setup for my dietery preferances, but you can change the Excel File in your computer to match your tastes.

| Day       | Start Time  | End Time    | Activity                                 |
| --------- | ----------- | ----------- | ---------------------------------------- |
| Monday    | 08:30:00 AM | 10:00:00 AM | Σοκολάτα/Αυγό/Δημητριακά                 |
| Monday    | 12:00:00 AM | 04:00:00 PM | Μοσχάρι κοκκινιστό με  πατάτες τηγανιτές |
| Monday    | 06:00:00 PM | 09:00:00 PM | Θράψαλα με μακαρόνια                     |
| Tuesday   | 08:30:00 AM | 10:00:00 AM | Σοκολάτα/Αυγό/Δημητριακά                 |
| Tuesday   | 12:00:00 AM | 04:00:00 PM | Κοτόπουλο με ρύζι                        |
| Tuesday   | 06:00:00 PM | 09:00:00 PM | Μπριάμ και τυρί φέτα                     |
| Wednesday | 08:30:00 AM | 10:00:00 AM | Σοκολάτα/Αυγό/Δημητριακά                 |
| Wednesday | 12:00:00 AM | 04:00:00 PM | Μπακαλιάρος με ρύζι                      |
| Wednesday | 06:00:00 PM | 09:00:00 PM | Σουπιές                                  |
| Thursday  | 08:30:00 AM | 10:00:00 AM | Σοκολάτα/Αυγό/Δημητριακά                 |
| Thursday  | 12:00:00 AM | 04:00:00 PM | Μπιφτέκι με πατάτες τηγανιτές            |
| Thursday  | 06:00:00 PM | 09:00:00 PM | Κοτόπουλο με ρύζι                        |
| Friday    | 08:30:00 AM | 10:00:00 AM | Σοκολάτα/Αυγό/Δημητριακά                 |
| Friday    | 12:00:00 AM | 04:00:00 PM | Ογκρατέν λαχανικών                       |
| Friday    | 06:00:00 PM | 09:00:00 PM | Μοσχάρι κοκκινιστό με  ρύζι              |
| Saturday  | 08:30:00 AM | 10:00:00 AM | Σοκολάτα/Αυγό/Δημητριακά                 |
| Saturday  | 12:00:00 AM | 04:00:00 PM | Μπριζόλα χοιρινή με ρύζι                 |
| Saturday  | 06:00:00 PM | 09:00:00 PM | Ψάρι φρέσκο με ψητά λαχανικά             |
| Sunday    | 08:30:00 AM | 10:00:00 AM | Σοκολάτα/Αυγό/Δημητριακά                 |
| Sunday    | 12:00:00 AM | 04:00:00 PM | Μοσχάρι κοκκινιστό με κους κους          |
| Sunday    | 06:00:00 PM | 09:00:00 PM | Μελιτζάνες παπουτσάκια                   |

Note: 
* Never attempt to change the Day columns or the program will not work, because the library used needs the days to be in English **only** and proper spelling.
* You can change the `Activity` or Food Column to add your favourite food from the various options Lesxh has available each day. But please follow my logging convention. (Check the Website to find out:https://www.auth.gr/weekly-menu/)


## Setup

1. Clone the repository to your local machine.

2. Install dependencies using.
Run the following commands
* To make sure everything is up to date :\
` sudo apt-get update `
* To install the library dependencies:\
` sudo apt-get install python3-pandas `\
` sudo apt-get install python3-datetime `
* To make sure everything is up to date again:
` sudo apt update && sudo apt upgrade `
 
* You can additionally restart your machine:
`sudo reboot` 

3. Modify the script to match your schedule Excel file path.
  
4. Add the script to your terminal startup file.\
Open the terminal and\
`nano ~/.bashrc`\
Go to the bottom of the nano file (where there is some empty space) and add the
```
echo -e "$(python3 [path to python script])"
```
Then save and exit with `Control + O` and `Enter`

You can check if this worked by using this command in the terminal to display the <<.bashrc>> file:
`source ~/.bashrc`


Now the script should automatically run when you open the terminal and display the following lines:

1. <<Παλικάρι, η λέσχη έχει (φαγητό)>> if food is currently beign served.
2. <<Έχει ξανά μάσα: (χρόνος μέχρι επόμενη διανομή)>> if food is to be served soon.
