# import libraries
pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis, httr, lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr)

# clear memory
rm(list = ls())

# import data
antibio1 <- rio::import("E:/Download_E/microbiology_data.xlsx")
# print(head(antibio1))

# define variables
organism <- antibio1$organism
spctype <- antibio1$spctype
hn <- antibio1$hn
drug <- antibio1[, 5:33]

# S = susceptible,R = resistant, blank cell = no data
# if S, + frrquency, if R, - frequency, if blank, 0
# convert to 1, 0, -1
drug[drug == "S"] <- 1
drug[drug == "R"] <- -1
drug[drug == ""] <- 0

#subset1: blood and Pseudomonas aeruginosa
subset_blood <- subset(antibio1, spctype == "blood") # select blood only

#plot heatmap for blood: y-axis represent each organism, x-axis represent each drug, color represent the frequency





