from neo4j import GraphDatabase, basic_auth                                      

# following lines connects the datbase from grapheneDB with user credentials and a session is created
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "cse1003"))
session = driver.session()

# creating datasets for 17 March 2020
session.run("CREATE (_17March2020:TRADEDATE {date:'17/03/2020'})")# running neo4j session on python and this line is creating node and its label is tradedate
#read from MCAP CSV file for that date NOTE: syntax for loadind csv files is the command below
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/17032020_MCap.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"17/03/2020\" and t.date = \"17/03/2020\"  AND c.LEAD='MCAP' CREATE (c)-[:MCAP_LEADER]->(t)")
#
#read from VOLUME CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/17032020_Volumes.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"17/03/2020\" and t.date = \"17/03/2020\" AND c.LEAD='VOLUME' CREATE (c)-[:VOL_LEADER]->(t)")

# inside company label there are 400 comapnies i.e 20 companies for each date


# creating datasets for 18 March 2020
session.run("CREATE (_18March2020:TRADEDATE {date:'18/03/2020'})")
#read from MCAP CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/18032020_MCap.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"18/03/2020\" and t.date = \"18/03/2020\"  AND c.LEAD='MCAP' CREATE (c)-[:MCAP_LEADER]->(t)")
#
#read from VOLUME CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/18032020_Volumes.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"18/03/2020\" and t.date = \"18/03/2020\" AND c.LEAD='VOLUME' CREATE (c)-[:VOL_LEADER]->(t)")




# creating datasets for 19 March 2020
session.run("CREATE (_19March2020:TRADEDATE {date:'19/03/2020'})")
#read from MCAP CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/19032020_MCap.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"19/03/2020\" and t.date = \"19/03/2020\"  AND c.LEAD='MCAP' CREATE (c)-[:MCAP_LEADER]->(t)")
#
#read from VOLUME CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/19032020_Volumes.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"19/03/2020\" and t.date = \"19/03/2020\" AND c.LEAD='VOLUME' CREATE (c)-[:VOL_LEADER]->(t)")



# creating datasets for 20 March 2020
session.run("CREATE (_20March2020:TRADEDATE {date:'20/03/2020'})")
#read from MCAP CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/20032020_MCap.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"20/03/2020\" and t.date = \"20/03/2020\"  AND c.LEAD='MCAP' CREATE (c)-[:MCAP_LEADER]->(t)")
#
#read from VOLUME CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/20032020_Volumes.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"20/03/2020\" and t.date = \"20/03/2020\" AND c.LEAD='VOLUME' CREATE (c)-[:VOL_LEADER]->(t)")



# creating datasets for 23 March 2020
session.run("CREATE (_23March2020:TRADEDATE {date:'23/03/2020'})")
#read from MCAP CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/23032020_MCap.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"23/03/2020\" and t.date = \"23/03/2020\"  AND c.LEAD='MCAP' CREATE (c)-[:MCAP_LEADER]->(t)")
#
#read from VOLUME CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/23032020_Volumes.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"23/03/2020\" and t.date = \"23/03/2020\" AND c.LEAD='VOLUME' CREATE (c)-[:VOL_LEADER]->(t)")



# creating datasets for 24 March 2020
session.run("CREATE (_24March2020:TRADEDATE {date:'24/03/2020'})")
#read from MCAP CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/24032020_MCap.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"24/03/2020\" and t.date = \"24/03/2020\"  AND c.LEAD='MCAP' CREATE (c)-[:MCAP_LEADER]->(t)")
#
#read from VOLUME CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/24032020_Volumes.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"24/03/2020\" and t.date = \"24/03/2020\" AND c.LEAD='VOLUME' CREATE (c)-[:VOL_LEADER]->(t)")



# creating datasets for 25 March 2020
session.run("CREATE (_25March2020:TRADEDATE {date:'25/03/2020'})")
#read from MCAP CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/25032020_MCap.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"25/03/2020\" and t.date = \"25/03/2020\"  AND c.LEAD='MCAP' CREATE (c)-[:MCAP_LEADER]->(t)")
#
#read from VOLUME CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/25032020_Volumes.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"25/03/2020\" and t.date = \"25/03/2020\" AND c.LEAD='VOLUME' CREATE (c)-[:VOL_LEADER]->(t)")


# creating datasets for 26 March 2020
session.run("CREATE (_26March2020:TRADEDATE {date:'26/03/2020'})")
#read from MCAP CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/26032020_MCap.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"26/03/2020\" and t.date = \"26/03/2020\" AND c.LEAD='MCAP' CREATE (c)-[:MCAP_LEADER]->(t)")
#
#read from VOLUME CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/26032020_Volumes.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"26/03/2020\" and t.date = \"26/03/2020\" AND c.LEAD='VOLUME' CREATE (c)-[:VOL_LEADER]->(t)")

# creating datasets for 27 March 2020
session.run("CREATE (_27March2020:TRADEDATE {date:'27/03/2020'})")
#read from MCAP CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/27032020_MCap.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"27/03/2020\" and t.date = \"27/03/2020\" AND c.LEAD='MCAP' CREATE (c)-[:MCAP_LEADER]->(t)")
#
#read from VOLUME CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/27032020_Volumes.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"27/03/2020\" and t.date = \"27/03/2020\" AND c.LEAD='VOLUME' CREATE (c)-[:VOL_LEADER]->(t)")


# creating datasets for 30 March 2020
session.run("CREATE (_30March2020:TRADEDATE {date:'30/03/2020'})")
#read from MCAP CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/30032020_MCap.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"30/03/2020\" and t.date = \"30/03/2020\" AND c.LEAD='MCAP' CREATE (c)-[:MCAP_LEADER]->(t)")
#
#read from VOLUME CSV file for that date
session.run("LOAD CSV WITH HEADERS FROM \"file:///C:/Users/Akash/Desktop/Akash/dbmsproject/ProjectWork/DataSamples/30032020_Volumes.csv\" AS row CREATE (n:Company) SET n = row")
# make relationship with date
session.run("MATCH (c:Company),(t:TRADEDATE) WHERE c.DATEVALUE = \"30/03/2020\" and t.date = \"30/03/2020\" AND c.LEAD='VOLUME' CREATE (c)-[:VOL_LEADER]->(t)")

#result1=session.run("MATCH (TRADEDATE)<-[:MCAP_LEADER]-(Company) RETURN distinct Company.SC_NAME")
#result2=session.run("MATCH (TRADEDATE)<-[:VOL_LEADER]-(Company) RETURN distinct Company.SC_NAME")



session.close()# closing neo4j session
