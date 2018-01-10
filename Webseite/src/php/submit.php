<?
    $servername = "122.goserver.host";
    $dbname = "web137_db2";
    $username = "web137_2";
    $password = "maxdubaum";

    $delayIds = str_split(" ", $_POST['ids'])
    

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

?>