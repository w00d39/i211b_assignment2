
# NBA Player Statistics Analysis
uses the NumPy library
## Project Overview

This project is designed to analyze NBA player statistics and identify the top 100 players based on various performance metrics. The analysis includes calculating shooting accuracy, average points per game, and average blocks and steals per game. The results are then printed for each metric, showcasing the top 100 players.

## Function Design and Implementation

The project is implemented using functions to handle data processing and analysis. The main functions are:

1. `statArrays()`
2. statsNBA()
3. getTop100Players()
4. printTop100()
5. top100Players()

### Function Descriptions

#### `statArrays()`

- **Purpose**: Reads NBA player statistics from a TSV file and converts them into NumPy arrays for further analysis.
- **Attributes**:
  - `playerArray`: Array of player names.
  - `seasonArray`: Array of seasons.
  - `fgmArray`: Array of field goals made.
  - `fgaArray`: Array of field goals attempted.
  - `tpmArray`: Array of three-pointers made.
  - `tpaArray`: Array of three-pointers attempted.
  - `ftmArray`: Array of free throws made.
  - `ftaArray`: Array of free throws attempted.
  - `ptsArray`: Array of points scored.
  - `minArray`: Array of minutes played.
  - `blkArray`: Array of blocks.
  - `gpArray`: Array of games played.
  - `stlArray`: Array of steals.
- **Returns**: A tuple containing all the arrays.

#### 

statsNBA()

- **Purpose**: Calculates various performance metrics for NBA players.
- **Attributes**:
  - 

mixedAccuracyForPlayers

: List containing player names, seasons, and mixed accuracy (average of field goal, three-pointer, and free throw accuracy).
  - 

avgPointsPerGameForPlayers

: List containing player names, seasons, and average points per game.
  - 

shootingAccuracyForPlayers

: List containing player names, seasons, and shooting accuracy.
  - 

avgBandSForPlayers

: List containing player names, seasons, average blocks, and average steals.
- **Returns**: A tuple containing the lists of calculated metrics.

#### 

getTop100Players(statArray, playerArray, seasonArray)



- **Purpose**: Identifies the top 100 players based on a given performance metric.
- **Parameters**:
  - `statArray`: Array of performance metric values.
  - `playerArray`: Array of player names.
  - `seasonArray`: Array of seasons.
- **Returns**: A list of tuples containing the top 100 players, their seasons, and their metric values.

