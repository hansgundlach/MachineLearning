library("ggvis")
df <- read.csv(file="datacollege.csv",head=TRUE,sep=";",stringsAsFactors= TRUE,dec= ",",row.names = NULL)
df$Highest.ACT = NULL
df$GPA <- as.numeric(as.character(df$GPA))
df$Highest.Combined.SAT.2400 <- as.numeric(as.character(df$Highest.Combined.SAT.2400))
df
df %>% ggvis(~df$GPA,~df$Highest.Combined.SAT.2400) %>% layer_points()
#mean finds the standard deviation 
mean  <- aggregate(df[, 1:2], list(df$App.Result), mean,na.rm=TRUE)
mean
print("This is the means for each group")
#this finds the standard deviation for each group and for each metric
stand <- aggregate(df[, 1:2], list(df$App.Result), sd,na.rm= TRUE)
stand
#first index is level or vertical

# we just want to calculate the mean of the 
calculate <- function(GPA,SAT)
{
  nCol <- length(mean[[2]])
  #probs is a list with the probabilities for each group Accepted Denied WAitlisted
  probs <- rep(0,nCol)
    #number of groups ie Accepted, Deied,Waitlisted
    size <- length(levels(factor(df$App.Result)))
    for(type in 1:size){
      
      
      myProbG <- pnorm(GPA,mean[[2]][[type]],stand[[2]][[type]])
      myProbG
      myProbSAT <- pnorm(SAT,mean[[3]][[type]],stand[[3]][[type]])
      
      myProb <- myProbG*myProbSAT
    probs[type] <- myProb
      
    }
    print(probs)
    which.max(probs)
    }
  calculate(1,24)