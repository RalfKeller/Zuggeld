<?php

$json_jobs = shell_exec("curl -u 39d09354c0474b5ea187b4ef20931431: https://app.scrapinghub.com/api/jobs/list.json?project=269022&spider=db&state=finished&count=2");
$jobs = json_decode($json_jobs);
$id_array = array();
foreach($jobs->jobs as $job){
    array_push($id_array, $job->id);
}

$items_array = array();

foreach($id_array as $id){
    $items = shell_exec("curl -u 39d09354c0474b5ea187b4ef20931431: https://storage.scrapinghub.com/items/".$id);
    array_push($items_array,$items);
}


// file_put_contents("text.json",$jobs);
?>