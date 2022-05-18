<?php
$ctnum="";
$ctnum = $_POST['ctnum'];
$conn = mysqli_connect('localhost','root','','user');
$sql = "SELECT * FROM regdata where aadhar_number='$ctnum'";
$res = mysqli_query($conn,$sql);
while($row = mysqli_fetch_assoc($res)) {
    if($row['aadhar_number']='$ctnum') {        
        $sql = "DELETE from regdata where aadhar_number='$ctnum'";
        $res = mysqli_query($conn, $sql);
    }
}
echo "<h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Thank You for using our services<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;Your ticket has been cancelled<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HOPE TO SEE YOU AGAIN &#128578</h1>";
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cancellation</title>
</head>
<body>
<style>
body {
    background-image: url('finalimg.jpg');
    background-repeat: no-repeat;
    position: absolute;
    background-size: 100%;
    background-position: center;
}
#else {
    color: white;
}
h1 {
    color: white;
    padding-top: 250px;
    padding-left: 450px;
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
<center style="padding-left: 510px;">
<a href="logout.html" class="buttonn">HOME</a>
</center>
</body>
</html>