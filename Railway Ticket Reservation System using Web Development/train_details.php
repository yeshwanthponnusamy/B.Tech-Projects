<?php
$conn = mysqli_connect('localhost','root','','user');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="table_styling.css">
</head>
<body>
<style>
table {
    width: 100%;
}
</style>
    <center>
        <h3><b>TRAINS AVAILABLE</b></h3>
    <table class="content-table">
        <tr>
            <th>TRAIN NUMBER</th>
            <th>TRAIN NAME</th>
            <th>DEPARTURE TIME</th>
            <th>ARRIVAL TIME</th>
            <th>FROM</th>
            <th>TO</th>
        </tr>
        <?php 
        $sql = "SELECT * from train";
        $res = mysqli_query($conn, $sql);
        while($row = mysqli_fetch_assoc($res)) {
        ?>
        <tr>
            <th><?php echo $row['train_number'] ?></th>
            <th><?php echo $row['train_name'] ?></th>
            <th><?php echo $row['dep_time'] ?></th>
            <th><?php echo $row['arr_time'] ?></th>
            <th><?php echo $row['from_st'] ?></th>
            <th><?php echo $row['to_st'] ?></th>
        </tr>
        <?php } ?>
    </table>
    </center>
</body>
</html>