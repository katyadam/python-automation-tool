# Python automation

## Functions

- removing files from a directory
    - based on date, type or size
    - date: dd.mm.yyyy-dd.mm.yyyy
    - type: pdf, docx, ...
    - size: %d-%d -- LOWER_BOUND-UPPER_BOUND

- distributing files from a directory to a subdirectory
    - based on date, type or size

- zipping files from a source

- unzipping files to a directory


### Commands
#### Removing
    python main.py -r [PATH] [DATE]                  [TYPES...]         [SIZE]<br>
                             dd.mm.yyyy-dd.mm.yyyy   <filetypes>       INTEGER-INTEGER in bytes
                                                     type1,type2,type3

#### Distributing
    python main.py -d [START PATH] [TYPE-DIRECTORY NAME...]

#### Zipping
    python main.py -z [WHAT] [NAME OF ZIP]

#### Unzipping 
    python main.py -u [WHAT] [WHERE]