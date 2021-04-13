# ##################################################
# DATA ANALYSIS MASTER'S THESIS ARMANDO HOLZKNECHT # 
####################################################

# INFO: Project is programmed using otree, variable coding can be seen in the python file
# or in the thesis

# PACKAGES
library(dplyr)
library(stringr) # for counting characters
library(ggplot2) # for graphical illustrations

#############################
# PREFACE - SETTING UP DATA #
#############################

# set working directory 
setwd('/Users/mandoholzknecht/MasterThesis/Data_Analysis')
list.files() # see files in directory


# Import data
data<- read.csv("~/MasterThesis/Data_Analysis/all_apps_wide_2021-04-10.csv", stringsAsFactors=FALSE)
data <- subset(data, participant._current_app_name == "Outro") # only those who completed the whole experiment
data <- subset(data, session.code == "diuycjxb") # subset of students
data <- subset(data, Intro.1.player.location =="school") # only in controlled school setting
colnames(data)

# select only data of interest
data <- data %>%
  select(participant.code, participant._index_in_pages, participant._current_app_name,
         participant.time_started,session.code, # participant and session info
         Intro.1.player.class_identifier, Intro.1.player.school_identifier, Intro.1.player.location, # App Intro
         Biases_T1.1.player.page_sequence_t1, Biases_T1.1.player.decoy_t1, Biases_T1.1.player.anchoring_t1_wtp,
         Biases_T1.1.player.framing_t1, Biases_T1.1.player.mental_accounting_t1,
         Biases_T1.1.player.conjunction_fallacy, # App Biases Treatment 1
         Biases_T2.1.player.page_sequence_t2, Biases_T2.1.player.decoy_t2, Biases_T2.1.player.anchoring_t2_buy,
         Biases_T2.1.player.anchoring_t2_wtp,Biases_T2.1.player.framing_t2,
         Biases_T2.1.player.mental_accounting_t2, # App Biases Treatment 2
         FinLit.1.player.interest_compounding, FinLit.1.player.real_interest, FinLit.1.player.diversification,
         FinLit.1.player.bond_pricing, FinLit.1.player.credit_interest, # App Financial Literacy
         Preferences.1.player.risk_preference, Preferences.1.player.fail_counter_heads, 
         Preferences.1.player.fail_counter_tails, Preferences.1.player.time_preference_1,
         Preferences.1.player.time_preference_2, Preferences.1.player.time_preference_3,
         Preferences.1.player.time_preference_4, Preferences.1.player.time_preference_5,
         Preferences.1.player.time_preference_6, Preferences.1.player.fail_counter_tp, # App Preferences
         Field_Behavior.1.player.gambling, Field_Behavior.1.player.general_risk, 
         Field_Behavior.1.player.saving, Field_Behavior.1.player.temptation,
         Field_Behavior.1.player.financial_troubles, Field_Behavior.1.player.fin_education_school,
         Field_Behavior.1.player.fin_education_parents, # App Field Behavior
         Demographics.1.player.age, Demographics.1.player.gender, Demographics.1.player.religion,
         Demographics.1.player.school_type, Demographics.1.player.school_level, Demographics.1.player.math_skill,
         Demographics.1.player.german_skill, Demographics.1.player.education_mother, 
         Demographics.1.player.education_father) # App Demographics

colnames(data) <- c("participant_code","page_index","current_app","time_started",
                    "session_code","class_identifier","school_identifier","location",
                    "page_sequence_t1","decoy_t1","anchoring_wtp_t1",
                    "framing_t1","mental_accounting_t1","conjunction_fallacy_t1","page_sequence_t2",
                    "decoy_t2","anchoring_buy_t2","anchoring_wtp_t2","framing_t2","mental_accounting_t2",
                    "finlit_interest_compounding","finlit_real_interst","finlit_diversification",
                    "finlit_bond_pricing","finlit_loan","risk_preference","qc_fails_heads","qc_fails_tails",
                    "time_preference_1","time_preference_2","time_preference_3","time_preference_4",
                    "time_preference_5","time_preference_6","qc_fails_time_preference","gambling",
                    "general_risk","saving","temptation","financial_worries","finedu_school",
                    "finedu_parents","age","gender","religion","school_type","school_level","math_skill",
                    "german_skill","edu_mother","edu_father")


####################################
# COMPUTING BEHAVIORAL CONSISTENCY #
####################################

data$decoy <- ifelse(data$decoy_t1==data$decoy_t2,1,0)
data$anchoring <- ifelse(data$anchoring_wtp_t1==data$anchoring_wtp_t2,1,0)
data$framing <- ifelse(data$framing_t1==data$framing_t2,1,0)
data$mental_accounting <- ifelse(data$mental_accounting_t1==data$mental_accounting_t2,1,0)
data$conjunction_fallacy <- ifelse(data$conjunction_fallacy_t1==0,1,0) #other way around because in otree
# it is coded that falling for conjunction fallacy is equal to one and zero if not. Consistent behavior means
# not falling for it and thus if subjects did not fall for it (i.e. it is 0), they now get a 1. 
data$behavioral_consistency <- rowSums(cbind(data$decoy,data$anchoring,
                                             data$framing,data$mental_accounting,
                                             data$conjunction_fallacy))

######################################
# COMPUTING FINANCIAL LITERACY SCORE #
######################################

data$financial_literacy <- NaN
data$financial_literacy_dontknow <- NaN

# iterating over every question and counting correct answers and dont know ticks 
for (i in 1:length(data$participant_code)){
  x = 0
  y = 0
  if (data$finlit_interest_compounding[i]==1){
    x = x + 1
  }
  if (data$finlit_real_interst[i]==1){
    x = x + 1
  }
  if (data$finlit_diversification[i]==1){
    x = x + 1
  }
  if (data$finlit_bond_pricing[i]==1){
    x = x + 1
  }
  if (data$finlit_loan[i]==1){
    x = x + 1
  }
  if (data$finlit_interest_compounding[i]==-1){
    y = y + 1
  }
  if (data$finlit_real_interst[i]==-1){
    y = y + 1
  }
  if (data$finlit_diversification[i]==-1){
    y = y + 1
  }
  if (data$finlit_bond_pricing[i]==-1){
    y = y + 1
  }
  if (data$finlit_loan[i]==1){
    y = y + 1
  }
  data$financial_literacy[i] <- x
  data$financial_literacy_dontknow[i] <- y
}

################################
# COMPUTE ECONOMIC PREFERENCES #
################################


# Risk preference is already given, the higher the number the more riskier the chosen gamble
data$risk <- data$risk_preference

# Fails in Risk Preference task
data$fails_risk_preference <- data$qc_fails_heads + data$qc_fails_tails

# Time preference: Compute new variable containing sequence of time preference tasks
data$time_preference_sequence <- paste(data$time_preference_1,data$time_preference_2,
                                       data$time_preference_3,data$time_preference_4,
                                       data$time_preference_5,data$time_preference_6, sep="")

data$time <- str_count(data$time_preference_sequence,"B")
# alternative without stringr package: lengths(regmatches(data$time_preference_sequence,gregexpr("B",data$time_preference_sequence)))

 # Fails in time preference task is also already given
data$fails_time_preference <- data$qc_fails_time_preference

###########################################
# COMPUTE FIELD BEHAVIOR AND DEMOGRAPHICS # 
###########################################

# already defined

################
# CONVERT TIME #
################

data$time_started <- as.POSIXlt.character(data$time_started) #convert character string to time format

#########################################
# HANDLING CLASS AND SCHOOL IDENTIFIERS #
#########################################

# School identifiers - suggestion
data$school_identifier <- tolower(data$school_identifier) # having everything in lower case
table(data$school_identifier) # see how many schools we have, what most inputs of schools were

participating_schools <- c("hak hall","pts innsbruck","handelsakademie hall",
                           "polytechnische schule innsbruck","pts ibk",
                           "polytechnische schule","poly","pts") # define a string of participating school
replacement <- c("hak hall","pts innsbruck","hak hall","pts innsbruck","pts innsbruck",
                 "pts innsbruck","pts innsbruck","pts innsbruck") # define a list by which the participating school should get replaced

part_repl_merge <- data.frame(part_school=participating_schools,replaced_by=replacement)

# standardizing school identifier
for (i in 1:nrow(data)){
  school_identifier <- data$school_identifier[i]
  for (j in 1:length(participating_schools)){
    participating_school <- participating_schools[j]
    replace_school <- replacement[j]
    
    list_similar_schools <- agrep(participating_school,data$school_identifier,value=T,max.distance = 0.1)
    
    if (school_identifier %in% list_similar_schools){
      x <- data$school_identifier[i]
      y <- replace_school
      print(paste(x,"replaced by",y))
      data$school_identifier[i] <- replace_school
    }
  }
}

# Class identifier
data$class_identifier <- tolower(data$class_identifier)

# adjust for a class in poly innsbruck
for (i in 1:nrow(data)){
  if (grepl("a",data$class_identifier[i]) & data$school_identifier[i]=="pts innsbruck"){
    data$class_identifier[i] <- "a"
  }
}

###########################################
# DESCRIPTIVE STATISTICS ABOUT THE SAMPLE #
###########################################

# Relative distribution across categories in demographics
round(table(data$gender)/nrow(data),2) # gender
round(table(data$religion)/nrow(data),2) # religion
round(table(data$school_type)/nrow(data),2) # school type
round(table(data$school_level)/nrow(data),2) # school level
round(table(data$math_skill)/nrow(data),2) # math skill
round(table(data$german_skill)/nrow(data),2) # german skill
round(table(factor(data$edu_mother, levels = c("1","2","3","4","5","0"),
                   labels = c("none","primary school","voccational school",
                              "A-levels","University","Don't Know")))/nrow(data),2) # education mother
round(table(factor(data$edu_father, levels = c("1","2","3","4","5","0"),
                   labels = c("none","primary school","voccational school"
                              ,"A-levels","University","Don't Know")))/nrow(data),2) # education father

# Relative across behavioral biases tasks / behavioral consistency
# decoy
round(table(data$decoy_t1)/nrow(data),2)
round(table(data$decoy_t2)/nrow(data),2)
round(table(data$decoy)/nrow(data),2)

# anchoring
summary(data$anchoring_wtp_t1)
summary(data$anchoring_wtp_t2)
table(data$anchoring)

# some have hak for example and tick ahs as school type


# Reversing math and german skill

table(data$math_skill)
table(6 - data$math_skill)
abs(data$math_skill)
rev(data$math_skill)
# outtakes
#group_bar_finlit <- ggplot(data, aes(behavioral_consistency,colour=gender)) + geom_density()
#group_bar_finlit

#plot()
