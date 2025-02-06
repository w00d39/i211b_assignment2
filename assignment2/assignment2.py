
import numpy as np

def statArrays (): 
    with open ('NBA_Player_Stats.tsv', 'r') as stats:
        stats = stats.readlines()
        stats = [line.strip().split('\t') for line in stats]
        statsHeader = stats[0]
    #general need throughout the program
    playerIndex = statsHeader.index('Player')
    seasonIndex = statsHeader.index('Season')

    #accuracyNBA + shootingNBA
    fgmIndex = statsHeader.index('FGM')
    fgaIndex = statsHeader.index('FGA')
    tpmIndex = statsHeader.index('3PM')
    tpaIndex = statsHeader.index('3PA')
    ftmIndex = statsHeader.index('FTM')
    ftaIndex = statsHeader.index('FTA')

    #pointsNBA
    ptsIndex = statsHeader.index('PTS')
    minIndex = statsHeader.index('MIN')

    #blocksNBA
    blkIndex = statsHeader.index('BLK')
    gpIndex = statsHeader.index('GP')
    stlIndex = statsHeader.index('STL')


    with open ('NBA_Column_Names.txt', 'r') as columnNames:
        columnNames = columnNames.readlines()   

    #assigning the arrays based from the columns
    #player arrays
    playerArray = np.array([row[playerIndex] for row in stats[1:]]) #player names
    seasonArray = np.array([row[seasonIndex] for row in stats[1:]]) #seasons

    #stat arrays
    fgmArray = np.array([float(row[fgmIndex]) for row in stats[1:]]) #field goals made
    fgaArray = np.array([float(row[fgaIndex]) for row in stats[1:]]) #field goals attempted
    tpmArray = np.array([float(row[tpmIndex]) for row in stats[1:]]) #three pointers made
    tpaArray = np.array([float(row[tpaIndex]) for row in stats[1:]]) #three pointers attempted
    ftmArray = np.array([float(row[ftmIndex]) for row in stats[1:]]) #free throws made 
    ftaArray = np.array([float(row[ftaIndex]) for row in stats[1:]]) #free throws attempted
    ptsArray = np.array([float(row[ptsIndex]) for row in stats[1:]]) #points 
    minArray = np.array([float(row[minIndex]) for row in stats[1:]]) #minutes
    blkArray = np.array([float(row[blkIndex]) for row in stats[1:]]) #blocks
    gpArray = np.array([float(row[gpIndex]) for row in stats[1:]]) #games played 
    stlArray = np.array([float(row[stlIndex]) for row in stats[1:]]) #steals



#     #returning the arrays
    return playerArray, seasonArray,fgmArray, fgaArray, tpmArray, tpaArray, ftmArray, ftaArray, ptsArray, minArray, blkArray, gpArray, stlArray


def statsNBA (): 
    #assigning the arrays to the variables from the statArrays function
    (playerArray, seasonArray, fgmArray, fgaArray, tpmArray, tpaArray,
    ftmArray, ftaArray, ptsArray, minArray, blkArray, gpArray, stlArray) = statArrays()


# accuracy = true positive / true negative + true positive

#A
    #accuracy for field goals
    fgAccuracy = fgmArray / ( np.sum(fgmArray) + np.sum(fgaArray))
    #accuracy for three pointers
    tpAccuracy = tpmArray / ( np.sum(tpmArray) + np.sum(tpaArray))
    #accuracy for free throws
    ftAccuracy = ftmArray / ( np.sum(ftmArray) + np.sum(ftaArray))
    #mixed accuracy
    mixedAccuracy = (fgAccuracy + tpAccuracy + ftAccuracy) / 3
    #mixed accuracy for players
    mixedAccuracyForPlayers = [playerArray, seasonArray, mixedAccuracy]

#B
    avgPoints = ptsArray / minArray #points per minute
    avgPointsPerGameForPlayers = [playerArray, seasonArray, avgPoints] #points per game for players

#C
    #shooting accuracy
    shootingAccuracy = (fgmArray + tpmArray + ftmArray) / (fgmArray + fgaArray + tpmArray + tpaArray + ftmArray + ftaArray)
    shootingAccuracy = np.where(np.isnan(shootingAccuracy), 0, shootingAccuracy) #replacing NaN with 0
    #shooting accuracy for players
    shootingAccuracyForPlayers = [playerArray, seasonArray, shootingAccuracy]
                        
#D
    #average blocks and steals
    avgBlocks = blkArray / gpArray
    avgSteals =  stlArray / gpArray #steals per game
    #average blocks and steals for players
    avgBandSForPlayers = [playerArray, seasonArray, avgBlocks, avgSteals]

    #returning the arrays
    return mixedAccuracyForPlayers, avgPointsPerGameForPlayers, shootingAccuracyForPlayers, avgBandSForPlayers



def getTop100Players (statArray, playerArray, seasonArray):
        
        #sorting the stat array in descending order
        sortedStat = np.argsort(statArray)[::-1]

        #getting the top 100 players
        top100 = sortedStat[:100]
        #getting the top 100 players with their respective player, season, and stat
        top100Players = [(playerArray[i], seasonArray[i], statArray[i]) for i in top100]
        #returning the top 100 players
        return top100Players

def printTop100 (title, top100Players):

    #`printing the title`
    print(title)
    #printing the top 100 players
    for player, season, value in top100Players:
        #printing the player, season, and value
        print(f"Player: {player}, Season: {season}, Value: {value}")
    print("\n") #new line
        


def top100Players (): 
        #assigning the arrays to the variables from the statsNBA function
        mixedAccuracyForPlayers, avgPointsPerGameForPlayers, shootingAccuracyForPlayers, avgBandSForPlayers = statsNBA()

        #getting the top 100 players for each stat
        topMixedAccuracy = getTop100Players(mixedAccuracyForPlayers[2], mixedAccuracyForPlayers[0], mixedAccuracyForPlayers[1])

        #getting the top 100 players for each stat
        topAVGPoints = getTop100Players(avgPointsPerGameForPlayers[2], avgPointsPerGameForPlayers[0], avgPointsPerGameForPlayers[1])

        #getting the top 100 players for each stat
        topShooting = getTop100Players(shootingAccuracyForPlayers[2], shootingAccuracyForPlayers[0], shootingAccuracyForPlayers[1])

        #getting the top 100 players for each stat
        topBandS = getTop100Players(avgBandSForPlayers[2], avgBandSForPlayers[0], avgBandSForPlayers[1])

        printTop100("Top 100 Players by Mixed Accuracy", topMixedAccuracy) #printing the top 100 players by mixed accuracy
        printTop100("Top 100 Players by Average Points Per Game", topAVGPoints) #printing the top 100 players by average points per game
        printTop100("Top 100 Players by Shooting Accuracy", topShooting) #printing the top 100 players by shooting accuracy
        printTop100("Top 100 Players by Average Blocks and Steals", topBandS) #printing the top 100 players by average blocks and steals

#calling the top100Players function which will call the statsNBA function
top100Players()







