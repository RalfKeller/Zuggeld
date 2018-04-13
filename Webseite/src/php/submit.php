<?php header('Access-Control-Allow-Origin: *');
    error_reporting(E_ALL);
    ini_set('display_errors', 'on');
    $servername = "localhost";
    $dbname = "web137_db2";
    $username = "web137_2";
    $password = "maxdubaum";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $userArray = json_decode($_POST['jsonUser'], true);
    $delayIds = json_decode($_POST['jsonDelays'], true);

    $attributes = "";
    $values = "";

    $first = 1;
    foreach ($userArray as $key => $value) {

        if($first == 1) {
            $attributes = $key;
            $values = "'" . $value . "'";
            $first = 0;
        }

        else{
            $attributes = $attributes . ", " . $key ;
            $values = $values . ", '" . $value . "'";
        }
    }

    $sql= "INSERT INTO db_user (" . $attributes . ") VALUES (" . $values . ")";

    if($conn->query($sql) == TRUE) {
        $last_id = $conn->insert_id;
        
        $values = "";
        echo $last_id;
        foreach($delayIds as $key => $value) {
            $sql = "INSERT INTO verspaetung_user (id_user, id_verspaetung) 
                    VALUES (" . $last_id . ", " . $value . ")";
            if(!($conn->query($sql) == TRUE)) {
                die("Error:" . $conn->error);
            }
        }
        
        echo "success";
    }

    else {
        die("Error:" . $conn->error);
    } 
?>