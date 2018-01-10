<?
    $servername = "s122.goserver.host";
    $dbname = "web137_db2";
    $username = "web137_2";
    $password = "maxdubaum";

    
    

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT id, start_bahnhof as von, ziel_bahnhof as nach, abfahrt as uhrzeit, datum FROM db_verspaetungen";
    $sth = mysqli_query($sql);
    $rows = array();

    while($r = mysqli_fetch_assoc($sth)) {
        $rows[] = r;
    }

    print json_encode($rows)



?>