<?php
    session_start();
    session_destroy();
    header('location: loginregister.html');
?>