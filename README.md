# Advent of Code 2024

## Setup

### Install dependencies
    
    uv sync

### Login to advent of code

    Go to: https://adventofcode.com/ and login with your account

### Get AOC token from browser cache

    mkdir -p ~/.config/aocd
    aocd-token > ~/.config/aocd/token

### Generate all files using the template

    poe bootstrap

## Usage

### Test solution against the examples

    poe test [DAY]

### Solve puzzle

    poe solve [DAY]

