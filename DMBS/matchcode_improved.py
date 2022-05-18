from neo4j import GraphDatabase, basic_auth
import matplotlib.pyplot as plt
import numpy as np

#usual starting of neo4j session
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "cse1003"))
session = driver.session()

#aim is to store names of all leaders in both aspects in separate lists for all ten days

#retrieve names for day1
result1=list(session.run("MATCH ( d:TRADEDATE{ date: \'17/03/2020\' } ) RETURN [(c)-[:VOL_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))
result2=list(session.run("MATCH ( d:TRADEDATE{ date: \'17/03/2020\' } ) RETURN [(c)-[:MCAP_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))

#retrieve names for day2
result3=list(session.run("MATCH ( d:TRADEDATE{ date: \'18/03/2020\' } ) RETURN [(c)-[:VOL_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))
result4=list(session.run("MATCH ( d:TRADEDATE{ date: \'18/03/2020\' } ) RETURN [(c)-[:MCAP_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))

#retrieve names for day3
result5=list(session.run("MATCH ( d:TRADEDATE{ date: \'19/03/2020\' } ) RETURN [(c)-[:VOL_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))
result6=list(session.run("MATCH ( d:TRADEDATE{ date: \'19/03/2020\' } ) RETURN [(c)-[:MCAP_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))

#retrieve names for day4
result7=list(session.run("MATCH ( d:TRADEDATE{ date: \'20/03/2020\' } ) RETURN [(c)-[:VOL_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))
result8=list(session.run("MATCH ( d:TRADEDATE{ date: \'20/03/2020\' } ) RETURN [(c)-[:MCAP_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))

#retrieve names for day5
result9=list(session.run("MATCH ( d:TRADEDATE{ date: \'23/03/2020\' } ) RETURN [(c)-[:VOL_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))
result10=list(session.run("MATCH ( d:TRADEDATE{ date: \'23/03/2020\' } ) RETURN [(c)-[:MCAP_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))

#retrieve names for day6
result11=list(session.run("MATCH ( d:TRADEDATE{ date: \'24/03/2020\' } ) RETURN [(c)-[:VOL_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))
result12=list(session.run("MATCH ( d:TRADEDATE{ date: \'24/03/2020\' } ) RETURN [(c)-[:MCAP_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))

#retrieve names for day7
result13=list(session.run("MATCH ( d:TRADEDATE{ date: \'25/03/2020\' } ) RETURN [(c)-[:VOL_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))
result14=list(session.run("MATCH ( d:TRADEDATE{ date: \'25/03/2020\' } ) RETURN [(c)-[:MCAP_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))

#retrieve names for day8
result15=list(session.run("MATCH ( d:TRADEDATE{ date: \'26/03/2020\' } ) RETURN [(c)-[:VOL_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))
result16=list(session.run("MATCH ( d:TRADEDATE{ date: \'26/03/2020\' } ) RETURN [(c)-[:MCAP_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))

#retrieve names for day9
result17=list(session.run("MATCH ( d:TRADEDATE{ date: \'27/03/2020\' } ) RETURN [(c)-[:VOL_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))
result18=list(session.run("MATCH ( d:TRADEDATE{ date: \'27/03/2020\' } ) RETURN [(c)-[:MCAP_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))

#retrieve names for day10
result19=list(session.run("MATCH ( d:TRADEDATE{ date: \'30/03/2020\' } ) RETURN [(c)-[:VOL_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))
result20=list(session.run("MATCH ( d:TRADEDATE{ date: \'30/03/2020\' } ) RETURN [(c)-[:MCAP_LEADER]->(d) WHERE c:Company | c.SC_NAME ] AS XXX"))


session.close()

#copy all the printed data into respective lists, since they can't be retrieved and used as such (given that result variables are single element lists)
#use appropriate indexing
day1_m=[]; day2_m=[]; day3_m=[]; day4_m=[]; day5_m=[]; day6_m=[]; day7_m=[]; day8_m=[]; day9_m=[]; day10_m=[];
day1_v=[]; day2_v=[]; day3_v=[]; day4_v=[]; day5_v=[]; day6_v=[]; day7_v=[]; day8_v=[]; day9_v=[]; day10_v=[];
day_v=[]; day_m=[]

for i in range(0,20):
    day1_v.append(result1[0][0][i])
    day1_m.append(result2[0][0][i])
    day2_v.append(result3[0][0][i])
    day2_m.append(result4[0][0][i])
    day3_v.append(result5[0][0][i])
    day3_m.append(result6[0][0][i])
    day4_v.append(result7[0][0][i])
    day4_m.append(result8[0][0][i])
    day5_v.append(result9[0][0][i])
    day5_m.append(result10[0][0][i])
    day6_v.append(result11[0][0][i])
    day6_m.append(result12[0][0][i])
    day7_v.append(result13[0][0][i])
    day7_m.append(result14[0][0][i])
    day8_v.append(result15[0][0][i])
    day8_m.append(result16[0][0][i])
    day9_v.append(result17[0][0][i])
    day9_m.append(result18[0][0][i])
    day10_v.append(result19[0][0][i])
    day10_m.append(result20[0][0][i])


#concatenate each of the two sets of lists into two new lists
day_v = day_v + day1_v + day2_v + day3_v + day4_v + day5_v + day6_v + day7_v + day8_v + day9_v + day10_v
day_m = day_m + day1_m + day2_m + day3_m + day4_m + day5_m + day6_m + day7_m + day8_m + day9_m + day10_m


#find unique elements(because we concatenate there might be repetitions, so to remove it we append the unique elements)
uqres_v=[]
uqres_m=[]

for item in day_v:
    if item not in uqres_v:
        uqres_v.append(item)

for item in day_m:
    if item not in uqres_m:
        uqres_m.append(item)

#search for no.of occurences in original lists and store the data in two dictionaries
dofv={}
dofm={}

for unit in uqres_v:
    count1=0
    for val in day_v:
        if val==unit:
            count1=count1+1
    dofv[unit]=count1

for unit in uqres_m:
    count2=0
    for val in day_m:
        if val==unit:
            count2=count2+1
    dofm[unit]=count2

#display of results of top level and bottom level companies
mm=min(list(dofm.values()))#minimum market capital
Mm=max(list(dofm.values()))#maximum market capital
mv=min(list(dofv.values()))
Mv=max(list(dofv.values()))

#lists to store the results
#marketlead=list(x for x in dofm.keys() and dofm[x]==Mm);
#marketlow=list(x for x in dofm.keys() and dofm[x]==mm);
#vollead=list(x for x in dofm.keys() and dofm[x]==Mv);
#vollo=list(x for x in dofm.keys() and dofm[x]==mv)
marketlead=[]
marketlow=[]
vollead=[]
vollow=[]
for x in dofm.keys():
    if dofm[x]==Mm:
        marketlead.append(x)
    elif dofm[x]==mm:
        marketlow.append(x)

for x in dofv.keys():
    if dofv[x]==Mv:
        vollead.append(x)
    elif dofv[x]==mv:
        vollow.append(x)
    


#to find companies that lead in both market capital as well as volume
#by lead, we mean with occurence value of more than 7

commonlist=[]
uncommoncos=[]
losercos=[]

for x in dofm.keys():
    for y in dofv.keys():
        if x==y:
            if dofm[x]>7 and dofv[x]>7:
                commonlist.append(x)# market capitals well as volume leader
                
for i in dofm.keys():
    if i not in commonlist:
        if dofm[i]>7:
            uncommoncos.append(i)

for i in dofv.keys():
    if i not in commonlist:
        if dofv[i]>7:
            uncommoncos.append(i)

for j in dofm.keys():
    if dofm[j] < 5:
        losercos.append(j)#loser companies are less than 5 occurences

for j in dofv.keys():
    if dofv[j]<5:
        losercos.append(j)



print("Stock market is a very unpredictable playfield these days. The stocks of even the most successful companies have an equal chance to fall down steep as does a\n",
      "low performing company to rise steeply. Investors find it difficult to choose a particular company based on the risk factor that one company that is at the top \n",
       "of the table can crumble down to the bottom, resulting in a bad investment.\n\n")
print("This project is an aid to such investors. It draws analysis from a database that consists of stock data taken from bseindia website. It analyses how frequently a \n",
      "company comes in the top positions within a period of ten days, and based on the analysis produced results. \n\n")
print("Here we count the occurences based on two factors: market capital and volume of shares. \n")

ans='y'
choice=0

while ans=='y' or ans=='Y':
    print("\n\n1. Graph ",
          "\n2. Companies that lead in market capital ",
          "\n3. Companies that perform poorly in market capital ",
          "\n4. Companies that lead in volume of shares ",
          "\n5. Companies that perform poorly in volume of shares ",
          "\n6. Companies that lead both in market capital as well as volume of shares ",
          "\n7. Companies that have performe poorly on the whole ",
          "\n8. Interpretation of results ",
          "\n9. Exit ")
    
    print("\n\nYour choice: ");
    choice=int(input())
    if choice==1:
        fig1=plt.figure(1);
        plt.bar(dofv.keys(),dofv.values());
        plt.title('LEADERS OF VOLUME')
        plt.xlabel('Companies')
        plt.ylabel('No. of times as leaders')
        plt.show()# it will show the plot whereas others will prepare the plot 

        fig2=plt.figure(2);
        plt.bar(dofm.keys(),dofm.values());
        plt.title('LEADERS OF MARKET CAPITAL')
        plt.xlabel('Companies')
        plt.ylabel('No. of times as leaders')
        plt.show()
        
    elif choice==2:
        print("LIST OF COMPANIES THAT LEAD IN ALL TEN DAYS IN THE ASPECT OF MARKET CAPITAL:\n")
        for item in marketlead:
            print(item)

    elif choice==3:
        print("LIST OF COMPANIES THAT PERFORMED POORLY IN ALL TEN DAYS IN THE ASPECT OF MARKET CAPITAL:\n")
        for item in marketlow:
            print(item)

    elif choice==4:
        print("LIST OF COMPANIES THAT LEAD IN ALL TEN DAYS IN THE ASPECT OF VOLUME:\n")
        for item in vollead:
            print(item)

    elif choice==5:
        print("LIST OF COMPANIES THAT PERFOMED POORLY IN ALL TEN DAYS IN THE ASPECT OF VOLUME:\n")
        for item in vollow:
            print(item)

    elif choice==6:
        print("LIST OF COMPANIES THAT LEAD IN BOTH ASPECTS:\n")
        for item in commonlist:
            print(item)

    elif choice==7:
        print("LIST OF POORLY PERFORMING COMPANIES:\n")
        for item in uncommoncos:
            print(item)

    elif choice==8:
        print("Thus, from the above analysis, we can infer the following points:\n\n")
        print("1. Investing in companies like ",commonlist[0],", ",commonlist[1]," etc. that lead in both market capital as well as volume of shares is a really valuable option.\n")
        print("2. The next lower level in the hierarchy can be with companies like ",uncommoncos[0],", ",uncommoncos[1]," etc. that are either only market capital leaders or only volume leaders.\n")
        print("3. Companies like ",losercos[0],", ",losercos[1]," etc. that occur in the top for less than 5 times are not so good to invest on, and they are practically the last choice of ",
              "companies you would like to go with.")

    elif choice==9:
        break

    else:
        print("Invalid choice. Pls enter a valid one.")
        continue
    
    print("\n\nDo you want to see more: ")
    ans=input();


print("Hope you now have a better understanding of how to choose your companies wisely. Thank you!!!")
        
#                                                                                      """END OF CODE"""                                                                                  




