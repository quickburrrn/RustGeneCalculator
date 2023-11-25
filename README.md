# Rust Game Gene Calculator
A program that help you find your best combination for your seeds

[![Python 3.6](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-360/)

***

## Table of content

- [Install](#install)
- [Usage](#Usage)
  - [Adding/Removing seeds](#addingremoving-seeds)
  - [Do stuff](#commands)
- [Known Issue](#known-issues-and-bugs)

***

## Install

Make shure that you have python-3 installed

You have two options:

#### Option 1

install the source code as a zip file and unzip the file

you should be fine from there

#### Option 2

Clone the GitHub repository

```bash
git clone https://github.com/Norkart/PlanWasher.git
```

***

## Usage

### Adding/Removing seeds

> [!Note]
>  Due to terrible performance it's recommended with 20 seeds max

Open `seeds.xml` located inside the base folder

to add seeds add following line:

```xml
 <Seed genes = "WGGWYH"/>
```

example of `seeds.xml`:
```xml
<?xml version="1.0"?>
<Seeds>
  <Seed genes = "HHGXGY"/>
  <Seed genes = "GHYWHH"/>
  <Seed genes = "XYHYGH"/>
  <Seed genes = "WYYGGW"/>
</Seeds>
```



### Commands

#### bruteforce

Finds the best combinations using bruteforce

This can take some time depending on how many seeds you have 

````
bruteforce
````

#### crossbreed

Crossbreeds the selected seeds

````
crossbreed
````

#### Seeds

Display the loaded seeds

```
seeds
```

#### Best

Finds the best seeds (NOT WORKING)

````
best
````

***

## known Issues and bugs

- Bad performance
