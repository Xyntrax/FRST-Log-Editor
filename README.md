# FRST Log Editor

A lightweight text editor built specifically for working with Farbar Recovery Scan Tool (FRST) logs.

Originally based on the **FRST Log Cleaner** by [**SkeletalDemise**](https://github.com/SkeletalDemise/FRST_log_cleaner), this project expands the original idea into a dedicated editor for reviewing and cleaning FRST logs. While it can be used as a regular text editor, its primary focus is making FRST logs easier to review.

## Features

* Automatic detection of `FRST.txt` and `Addition.txt`
* Clean all opened FRST logs in a single operation using a keyboard shortcut
* Filters known clean strings/entries
* Generates a `Whitelisted_Strings.txt` document containing every filtered entry for later review
* Syntax highlighting for commonly reviewed FRST strings
* Built-in search
* Dark and light themes

## Highlighted Indicators

The editor highlights commonly reviewed FRST strings, including:

* `<==== ATTENTION`
* `No File`
* `File not signed`
* `[not found]`
* `[X]`
* `Hidden`
* `no ImagePath`
* `detected!`
* `powershell`

Each indicator is color coded based on its priority to make manual review easier.

## How Cleaning Works

The editor compares each line against a list of clean strings representing known benign FRST entries.

If a line matches a clean string on the list, it is removed from the logs.

Filtered entries are not discarded. Instead, they are collected into a separate `Whitelisted_Strings.txt` document, allowing every removed entry to be reviewed at any time.

## Keyboard Shortcuts

| Shortcut               | Action                                                   |
| ---------------------- | -------------------------------------------------------- |
| **Ctrl + O**           | Open file(s)                                             |
| **Ctrl + S**           | Save current tab                                         |
| **Ctrl + Shift + S**   | Save As                                                  |
| **Ctrl + W**           | Close tab                                                |
| **Ctrl + Q**           | Exit                                                     |
| **Ctrl + T**           | New tab                                                  |
| **Ctrl + Shift + C**   | Clean all opened FRST logs                               |
| **Ctrl + Shift + R**   | Revert the current FRST log to its original loaded state |
| **Ctrl + Shift + W**   | View `Whitelisted_Strings.txt`                           |
| **Ctrl + Tab**         | Next tab                                                 |
| **Ctrl + Shift + Tab** | Previous tab                                             |
