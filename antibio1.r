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
drugs <- antibio1[, 5:33]

# S = susceptible,R = resistant, blank cell = no data
# if S, + frrquency, if R, - frequency, if blank, 0
# convert to 1, 0, -1
# drugs[drugs == "S"] <- 1
# drugs[drugs == "R"] <- -1
# drugs[drugs == ""] <- 0




#subset1: blood and Pseudomonas aeruginosa
subset_blood <- subset(antibio1, spctype == "blood") # select blood only


# plot heatmap for blood: y-axis represent each organism,
# x-axis represent each drug, color represent the frequency

# Heatplot from Base R
# using default mtcars dataset from the R
x <- as.matrix(as.numeric(antibio1))

# custom colors
new_colors <- colorRampPalette(c("cyan", "darkgreen"))

# plotting the heatmap
plt <- heatmap(x,
			# assigning new colors
			col = new_colors(100),
				
			# adding title
			main = "Heatmap for mtcars dataset",
				
			# adding some margin so that
			# it does not drawn over the
			# y-axis label
			margins = c(5,10),
				
			# adding x-axis labels
			xlab = "variables",
				
			# adding y-axis labels
			ylab = "Car Models",
				
			# to scaled the values into
			# column direction
			scale = "column"
)




