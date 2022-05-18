<?php
    session_start();
    $id = $_POST['id'];
    $pass= $_POST['pass'];
    $con= mysqli_connect('localhost', 'root', '','user');
    $login= "SELECT * from reg where uid='$id'";
    $res = mysqli_query($con, $login);
    $num= mysqli_num_rows($res);
    if($num==1) {
        header('location: logout.html');
    }
    else {
        echo "Invalid Login..The user doesnt exists..Sign up first";
    }
?>