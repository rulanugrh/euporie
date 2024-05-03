![banner](.github/banner.png)

## Before Running
```bash
$ pip install -r requirements.txt
# If not working you can running this command

$ python -m pip install requirements.txt

# or can use this command
$ py -m pip install requrements.txt
```

## Command Line
**_to showing help command_**
```cmd
$ python main.py help
+----------+-----------------------------------------------------------------+
| flag     | description                                                     |
+==========+=================================================================+
| help     | print help command                                              |
+----------+-----------------------------------------------------------------+
| show     | showing about info dataframe or graph [inflation / cpi / graph] |
+----------+-----------------------------------------------------------------+
| generate | generated preparation data or mean data                         |
+----------+-----------------------------------------------------------------+
```

**_to print `show help` command_**
```cmd
$ python main.py show help

+-----------------+------------------------------+------------------------------------------------------------------------------+
| flag            | description                  | example usage                                                                |
+=================+==============================+==============================================================================+
| inflation       | show about info or inflation | ex. python main.py show inflation [ info / dataframe ]                       |
+-----------------+------------------------------+------------------------------------------------------------------------------+
| cpi             | show about info or cpi       | ex. python main.py show info [ info / dataframe ]                            |
+-----------------+------------------------------+------------------------------------------------------------------------------+
| graph inflation | show graph inflation         | ex. python main.py show graph inflation [ 2020 / 2021 / 2022 / 2023 / 2024 ] |
+-----------------+------------------------------+------------------------------------------------------------------------------+
```

**_to print `generate help` command_**
```cmd
$ python main.py generate help

+-----------+--------------------------------------+---------------------------------------------------------------+
| flag      | description                          | example usage                                                 |
+===========+======================================+===============================================================+
| inflation | generated data preparation inflation | ex. python main.py generated inflation [ preparation / mean ] |
+-----------+--------------------------------------+---------------------------------------------------------------+
```