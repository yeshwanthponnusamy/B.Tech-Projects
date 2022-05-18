<?php

//initialize all of the variables with a null value 

$boarding=$destination=$train_name=$train_number="";
$pass_name1=$age1=$gender1=$aadhar_number1="";
$pass_name2=$age2=$gender2=$aadhar_number2="";
$pass_name3=$age3=$gender3=$aadhar_number3="";
$pass_name4=$age4=$gender4=$aadhar_number4="";
$pass_name5=$age5=$gender5=$aadhar_number5="";
$date="";

//assign the registration form data a specific variable

$boarding= $_POST['boarding'];
$destination= $_POST['destination'];
$train_name= $_POST['tname'];
$train_number= $_POST['tnum'];
$date= $_POST['tdate'];
$pass_name1=$_POST['p1'];
$age1=$_POST['age1'];
$gender1=$_POST['gender1'];
$aadhar_number1=$_POST['aadhar_no1'];
$pass_name2=$_POST['p2'];
$age2=$_POST['age2'];
$gender2=$_POST['gender2'];
$aadhar_number2=$_POST['aadhar_no2'];
$pass_name3=$_POST['p3'];
$age3=$_POST['age3'];
$gender3=$_POST['gender3'];
$aadhar_number3=$_POST['aadhar_no3'];
$pass_name4=$_POST['p4'];
$age4=$_POST['age4'];
$gender4=$_POST['gender4'];
$aadhar_number4=$_POST['aadhar_no4'];
$pass_name5=$_POST['p5'];
$age5=$_POST['age5'];
$gender5=$_POST['gender5'];
$aadhar_number5=$_POST['aadhar_no5'];

//connecting to the database

$connect= mysqli_connect('localhost','root', '','user');

//inserting the values into the tables 
if(!empty($pass_name1) && !empty($age1) && !empty($gender1) && !empty($aadhar_number1)) {
    $sql= "INSERT into regdata(pass_name,age,gender,aadhar_number) values('$pass_name1','$age1','$gender1','$aadhar_number1')";
    $res= mysqli_query($connect,$sql);  
}
if(!empty($pass_name2) && !empty($age2) && !empty($gender2) && !empty($aadhar_number2)) {
    $sql= "INSERT into regdata(pass_name,age,gender,aadhar_number) values('$pass_name2','$age2','$gender2','$aadhar_number2')";
    $res= mysqli_query($connect,$sql);  
}
if(!empty($pass_name3) && !empty($age3) && !empty($gender3) && !empty($aadhar_number3)) {
    $sql= "INSERT into regdata(pass_name,age,gender,aadhar_number) values('$pass_name3','$age3','$gender3','$aadhar_number3')";
    $res= mysqli_query($connect,$sql);  
}
if(!empty($pass_name4) && !empty($age4) && !empty($gender4) && !empty($aadhar_number4)) {
    $sql= "INSERT into regdata(pass_name,age,gender,aadhar_number) values('$pass_name4','$age4','$gender4','$aadhar_number4')";
    $res= mysqli_query($connect,$sql);  
}
if(!empty($pass_name5) && !empty($age5) && !empty($gender5) && !empty($aadhar_number5)) {
    $sql= "INSERT into regdata(pass_name,age,gender,aadhar_number) values('$pass_name5','$age5','$gender5','$aadhar_number5')";
    $res= mysqli_query($connect,$sql);  
}
echo "<h1>Your response has been successfully submitted<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;Your ticket has been booked<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HAVE A SAFE JOURNEY &#128578</h1>";

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>REGISTERED</title>
    <link rel="stylesheet" href="button_style.css">
</head>
<body>
<style>
body {
    background-image: url('thankyoureg.jpg');
    background-repeat: no-repeat;
    position: absolute;
    background-size: 100%;
    background-position: center;
}
h1 {
    color: white;
    padding-top: 250px;
    padding-left: 430px;
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
<center style="padding-left: 450px;">
<a href="logout.html" class="buttonn">HOME</a>
</center>
</body>
</html>