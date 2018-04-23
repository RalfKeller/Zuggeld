<?php header('Access-Control-Allow-Origin: *');
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

    $sql = "SELECT id, start_bahnhof as von, ziel_bahnhof as nach, echte_ankunft, ankunft, datum, datum_ankunft, zug_nummer, zug_typ, abfahrt FROM db_verspaetungen";
    $result = $conn->query($sql);
    $rows = array();

    while($r = $result->fetch_assoc()) {
        $rows[] = $r;
    }

    print json_encode($rows)

?>