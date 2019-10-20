require(devtools)
install_github('davidcarslaw/openair')

library(openair)
kc1 <- importAURN(site = "kc1", year = 2011:2012)
head(kc1)

write.table(mydata,"C:/Users/Oliver/Hack.txt", sep="\t")
