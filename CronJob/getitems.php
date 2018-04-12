<?php

$DBServer = 's122.goserver.host:3306'; // e.g 'localhost' or '192.168.1.100'
$DBUser   = 'web137_2';
$DBPass   = 'maxdubaum';
$DBName   = 'web137_db2';

$conn = new mysqli($DBServer, $DBUser, $DBPass, $DBName);
 
// check connection
if ($conn->connect_error) {
  trigger_error('Database connection failed: '  . $conn->connect_error, E_USER_ERROR);
}
else{
    echo "success";
}

$json_jobs = shell_exec("curl -u 39d09354c0474b5ea187b4ef20931431: https://app.scrapinghub.com/api/jobs/list.json?project=269022&spider=db&state=finished&count=2");
$jobs = json_decode($json_jobs);
$id_array = array();
foreach($jobs->jobs as $job){
    array_push($id_array, $job->id);
}

$items_array_array = array();

foreach($id_array as $id){
    $items = shell_exec("curl -u 39d09354c0474b5ea187b4ef20931431: https://storage.scrapinghub.com/items/".$id."?format=json");
    array_push($items_array_array,$items);
}


foreach($items_array_array as $json_item){
    
    $items_array = json_decode($json_item);

    foreach($items_array as $item ){

        $start_station = $item->start_station;
        $end_station = $item->end_station;
        $realtime = trim($item->realtime);
        $prognose = trim($item->prognose);
        $datum = $item->datum;
        $arrival_date = $item->arrival_date;
        $train_number = $item->train_number;
        $train_type = $item->train_type;
        $departure_time = $item->departure_time;
        $departure_time = trim($departure_time);

        if(is_null($train_number)){
            $train_number = "not found";
        }
        if(is_null($train_type)){
            $train_type = "not found";
        }
        if(is_null($realtime)){
            $realtime = $prognose;
        }


        if(!($stmt = $conn->prepare("INSERT INTO db_verspaetungen (start_bahnhof, ziel_bahnhof, echte_ankunft , ankunft, datum, datum_ankunft, zug_nummer, zug_typ, abfahrt) VALUES (?,?,?,?,?,?,?,?,?) ON DUPLICATE KEY UPDATE start_bahnhof = VALUES(start_bahnhof)"))){
            echo "Prepare failed: (" . $mysqli->errno . ") " . $mysqli->error;
        }
        else{
            // echo "Prepare WIN!";
        }

        // if(!$stmt){
        //     echo "ERROR!";
        // }

        if(!($stmt->bind_param('sssssssss',$start_station,$end_station,$realtime,$prognose,$datum,$arrival_date,$train_number,$train_type,$departure_time[0]))){
            echo "Binding parameters failed: (" . $stmt->errno . ") " . $stmt->error;
        }
        else{
            // echo "Binding WIN!";
        }

        if (!$stmt->execute()) {
            echo "Execute failed: (" . $stmt->errno . ") " . $stmt->error;
            echo <br>;
            echo $prognose;
        }
        else{
            // echo "Execute WIN!";
        }

        if($stmt->affected_rows === 0) exit('No rows updated');
        else{
            // echo "Rows affected:" . $stmt->affected_rows;
        }


        // if(is_null($realtime)) {
        //     $sql="INSERT INTO db_verspaetungen (start_bahnhof, ziel_bahnhof, ankunft, datum, datum_ankunft, zug_nummer, zug_typ, abfahrt) VALUES ('$start_station','$end_station','$prognose','$datum','$arrival_date',
        // '$train_number','$train_type',$departure_time[0]) ON DUPLICATE KEY UPDATE start_bahnhof = VALUES(start_bahnhof)";
        // }
        // else{
        //     $sql="INSERT INTO db_verspaetungen (start_bahnhof, ziel_bahnhof, echte_ankunft, ankunft, datum, datum_ankunft, zug_nummer, zug_typ, abfahrt) VALUES ('$start_station','$end_station','$realtime','$prognose','$datum','$arrival_date',
        // '$train_number','$train_type','$departure_time[0]') ON DUPLICATE KEY UPDATE echte_ankunft = VALUES(realtime)";
        // }
        

        

        // if($conn->query($sql) === false) {
        //     echo 'Wrong SQL: ' . $sql . ' Error: ' . $conn->error;
        //     trigger_error('Wrong SQL: ' . $sql . ' Error: ' . $conn->error, E_USER_ERROR);
        //   } else {
        //     $last_inserted_id = $conn->insert_id;
        //     $affected_rows = $conn->affected_rows;
        //     echo $last_inserted_id . "\n";
        //     echo $affected_rows . "\n";
        //   }
    }


}


// file_put_contents("text.json",$jobs);
?>