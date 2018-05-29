##5/28/18 Euro Cup qualifiers #5/29/18 

wcr=read.csv("wcr.csv")
str(wcr)
write.csv(wcr,file="wcr1.csv")
wc14q=read.csv("wc14q.csv")
head(wc14q)
wc14q['date']

library(stringr)
match_date=substr(wc14q$date,start=4,stop=5)
wc14q1=cbind(wc14q,match_date)

write.csv(wc14q1,file="wc14q1.csv")

wc14q=read.csv("wc14q2.csv")
head(wc14q)

library(plyr)
names(wc14q)

#score differentials 
#team 1
t1_score_diff<-ddply(wc14q,.(team1),plyr::summarize,t1_sd_sum=sum(score_diff_t1))
t1_score_diff

#team 2
t2_score_diff<-ddply(wc14q,.(team2),plyr::summarize,t2_sd_sum=sum(score_diff_t2))
t2_score_diff

#weighted date differentials
#team 1
t1_score_diff_date<-ddply(wc14q,.(team1),plyr::summarize,t1_sd_sum_date=sum(sd1_weight))
t1_score_diff_date 

#team 2 
t2_score_diff_date<-ddply(wc14q,.(team2),plyr::summarize,t2_sd_sum_date=sum(sd2_weight))
t2_score_diff_date


#combine columns
team_ratings=cbind(t1_score_diff,t2_score_diff,t1_score_diff_date,t2_score_diff_date)

team_ratings$team_score_diff=team_ratings$t1_sd_sum+team_ratings$t2_sd_sum
team_ratings$team_score_diff_date=team_ratings$t1_sd_sum_date+team_ratings$t2_sd_sum_date

team_ratings1=subset(team_ratings,select=c("team1","team_score_diff","team_score_diff_date"))
write.csv(team_ratings1,file="team_ratings.csv")



