# Stochastic Agent Simulation

This repository collects a series of simulation methods and models I’ve developed and studied through the UC Berkeley MSSE program.  
Each file demonstrates a different numerical or stochastic simulation technique — ranging from basic random-walk models to energy-based Monte Carlo methods.

---

## Overview

The simulations in this repository explore **stochastic processes**, **agent dynamics**, and **energy-based systems** in both Python and C++.  
They serve as educational tools to visualize, analyze, and understand the mathematical and physical behaviors that emerge from probabilistic motion and interaction models.

---

## Contents

| File | Description |
|------|--------------|
| `agent_motion_simulation.py` | Simulates random motion of agents in 2D space, illustrating stochastic diffusion and boundary effects. |
| `stochastic_agent_dynamics.py` | Models interacting agents with tunable randomness and movement rules, exploring emergent collective behavior. |
| `energy_analysis_utils.py` | Utility functions for energy calculations and trajectory visualization in agent-based simulations. |
| `particle_simulation_visualizer.py` | Visualization and animation module to track particle trajectories and simulate system evolution. |
| `monte_carlo_lennard_jones.cpp` | Implements a **Lennard-Jones Monte Carlo simulation** for molecular systems, using C++ and `matplotlibcpp` to visualize particle positions and energy convergence. |
| `matplotlibcpp.h` | Embedded C++ header for Python–C++ plotting integration via Matplotlib. |

---

## Simulation Highlights

- **Random Walks** and Brownian motion  
- **Metropolis Monte Carlo** energy minimization  
- **Lennard–Jones potential** modeling of molecular interactions  
- **Real-time visualization** with Python Matplotlib and C++ bindings  
- **Energy evolution tracking** and spatial system analysis  

---

## Concepts Illustrated

- Stochastic processes and noise-driven systems  
- Potential energy landscapes and particle interactions  
- Numerical simulation and algorithmic stability  
- Bridging **Python** and **C++** for high-performance simulation and visualization  

---

## Usage

### Python Simulations
```bash
python3 agent_motion_simulation.py
python3 stochastic_agent_dynamics.py
