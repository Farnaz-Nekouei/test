# Traffic Digital Twin for Baden-Württemberg & Bayern
Purpose:
- Real-world multi-source traffic fusion
- Streaming digital twin
- BASt + HERE + OSM + DWD integration
- Time-series + regression + graph modeling
  
## Overview

This repository implements a real-time traffic digital twin system integrating:

- BASt traffic counts
- HERE real-time traffic API
- OpenStreetMap road topology

Regions:
- Baden-Württemberg
- Bayern

## System Components

1. Data ingestion (API + CSV)
2. Data fusion (multi-source alignment)
3. Streaming (Kafka-compatible)
4. Digital twin state modeling
5. Analytics & prediction
6. Visualization

## Data Sources

- BASt (traffic counts)
- HERE Technologies (real-time traffic)
- OpenStreetMap (road graph)

## Key Variables

| Variable | Description | Unit |
|----------|------------|------|
| flow (q) | vehicles per hour | veh/h |
| speed (v) | average speed | km/h |
| density (k) | vehicles per km | veh/km |

## Fundamental Equation

Traffic flow theory:

q = k * v

## Run

pip install -r requirements.txt
python ingestion/here_loader.py