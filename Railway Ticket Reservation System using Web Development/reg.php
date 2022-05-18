<?php
    session_start();
    $uid = $_POST['uid'];
    $uem = $_POST['uem'];
    $upas = $_POST['upas'];
    $conn = mysqli_connect('localhost', 'root', '', 'user');
    $sql1= "SELECT * from reg where uid='$uid'";
    $res= mysqli_query($conn, $sql1);
    $num= mysqli_num_rows($res);
    if($num==1 ) {
        echo "User already exists";
        header('Location: loginregister.html');
    }
    else {
        $reg= "INSERT INTO reg(uid, uem, upas) values('$uid', '$uem','$upas')";  
        mysqli_query($conn, $reg);
        echo "Registered successfully";
    }
?>