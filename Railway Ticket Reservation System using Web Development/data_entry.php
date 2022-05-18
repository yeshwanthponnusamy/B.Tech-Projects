<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DATA ENTRY</title>
</head>
<body>
<form action="data_entry.php" method="POST">
    TRAIN NAME: <input type="text" name="tname"><br>
    TRAIN NUMBER: <input type="text" name="tnumber"><br>
    DEPARTURE TIME: <input type="text" name="deptime"><br>
    ARRIVAL NAME: <input type="text" name="arrtime"><br>
    from : <input type="text" name="fromm"><br>
    to: <input type="text" name="too"><br>
    <input type="submit" value="submit the data" name="submit">
</form>
</body>
</html>

<?php

$train_name=$train_number=$dep_time=$arr_time="";
if(isset($_POST['submit'])) {
    echo "DATA IS TO BE INSERTED RIGHT NOW AND RIGHT HERE";
    $train_name= $_POST['tname'];
    $train_number= $_POST['tnumber'];
    $dep_time=$_POST['deptime'];
    $arr_time=$_POST['arrtime'];
    $fromm = $_POST['fromm'];
    $too = $_POST['too'];
    $connect= mysqli_connect('localhost','root','','user');
    $sql= "INSERT into train(train_number,train_name,dep_time,arr_time,from_st,to_st) values('$train_number','$train_name','$dep_time','$arr_time','$fromm','$too')";
    $res= mysqli_query($connect,$sql);
    echo "DATA INSERTED SUCCESSFULLY....IF YOU CANT SEE THE INSERTED DATA IN THE DATABASE THEN THERE IS SOME ISSUE WHICH YOU MIGHT NOW KNOW AS OF NOW";
}
else {
    echo "DATA NOT INSERTED OR SOME ISSUE IS THERE WITH THE CODE IN DATA INSERTION";
}
?>