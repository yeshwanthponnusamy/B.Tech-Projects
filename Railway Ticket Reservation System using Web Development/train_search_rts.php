<?php

$from = $_POST['from'];
$to = $_POST['to'];
$con = mysqli_connect('localhost','root','','user');
$sql = "SELECT * FROM train";
$res = mysqli_query($con, $sql);
echo "<center>";
    echo "<h3>TRAINS AVAILABLE FROM <b>$from</b> TO <b>$to</b> </h3>";
echo "</center>";
echo "<table class='content-table'>";
echo "<tr>";
    echo "<th>TRAIN NUMBER</th>";
    echo "<th>TRAIN NAME</th>";
    echo "<th>DEPARTURE TIME</th>";
    echo "<th>ARRIVAL TIME</th>";
    echo "<th>FROM</th>";
    echo "<th>TO</th>";
echo "</tr>";
while($row = mysqli_fetch_assoc($res)) {
    if($from==$row['from_st'] && $to==$row['to_st']) {
            echo "<tr>";
                echo "<th>" .$row['train_number']. "</th>";
                echo "<th>" .$row['train_name']. "</th>";
                echo "<th>" .$row['dep_time']. "</th>";
                echo "<th>" .$row['arr_time']. "</th>";
                echo "<th>" .$row['from_st']. "</th>";
                echo "<th>" .$row['to_st']. "</th>";
        }
    }
echo "</table>";

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SEARCH DETAILS</title>
    <link rel="stylesheet" href="table_styling.css">
</head>
<body>
<style>
table {
    width: 100%;
}
a.buttonn{
    display: inline-block;
    padding: 0.3em 1.2em;
    margin: 0 0.3em 0.3em 0;
    border-radius: 2em;
    box-sizing: border-box;
    text-decoration: none;
    font-weight: 300;
    color: #FFFFFF;
    left: 500px;
    background-color: #4eb5f1;
    text-align: center;
    transition: all 0.2s;
    left: 900px;
}
</style>
<center style="padding-left: 40px;">
<a href="loginregister.html" class="buttonn">Login to Book a ticket</a>
</center>
</body>
</html>