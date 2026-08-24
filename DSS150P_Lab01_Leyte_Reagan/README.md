# DSS150P Lab 01 - Data Engineering

## Student Information
- Name: Reagan Leyte
- Section: [CM17]
- Date Started: [8/23/2026]

## Overview
This repository contains the completed Laboratory Activity #1 for DSS150P.

## Repository Structure

DSS150P_Lab01_Leyte_Reagan/
├── data/
│ ├── raw/
│ │ ├── customers.csv
│ │ ├── orders.json
│ │ ├── products.parquet
│ │ └── api_snapshot.json
│ └── evidence/
│ ├── version_check.txt
│ ├── packages_installed.txt
│ ├── profile_output.txt
│ └── api_output.txt
├── docs/
│ ├── lifecycle_map.md
│ ├── source_inventory.md
│ ├── source_profile.md
│ ├── data_contract.yaml
│ └── reflection.md
├── sql/
│ └── 01_create_schema.sql
├── src/
│ ├── verify_environment.py
│ ├── profile_sources.py
│ └── inspect_api.py
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md

Should be correct I think
I have been trying to make Docker work but nothing is owrking so I only hope sir actually tackles how to install a Docker again.

## How to Run

### 1. Setup Virtual Environment
```bash
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt

AI: ChatGPT/DeepSeek/VSC AI
Docker- I tried using AI but I just gave up, if I remember correctly the parts that needs a Docker here is not done because I just gave up and went to sleep. I think the ones that needed to run SQL is the ones that I didnt manage to do. 
Reflection- I made it summarize the entire thing because I did this between other subjects so I forgot some of the parts already, after summarizing I made the reflection using it.
Code- I find the code in Google, ask AI if its useful for the part I was making and then use it when its applicable, if I am stuck in a code for a while like the ones in profile_sources.py I ask for the built in AI in VSC to help me fix the errors. I switch between ChatGPT and Deepseek because the answer they gave me sometimes are contradicting so when they do contradict I can double check it.