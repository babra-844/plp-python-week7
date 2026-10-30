
# Week 7 Python Assignment

## Project Description

This project demonstrates Python list operations,
loops, conditions, and basic error prevention.

## Project Files

- list_warmup.py - Demonstrates list indexing,
  append(), remove(), and len().
- shopping_list.py - Creates an interactive
  shopping list manager using a loop.
- list_report.py - Displays numbered items,
  counts item names, and finds the longest name.
- screenshots/ - Contains screenshots showing
  each Python program running.

## Why Check `in` Before Using `.remove()`?

Checking whether an item exists before calling
.remove() helps prevent errors in Python.

If an item does not exist, .remove() raises a
ValueError. Using the `in` operator first makes
the program safer and prevents unexpected crashes.
