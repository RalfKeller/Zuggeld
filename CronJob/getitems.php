<?php

$json_jobs = shell_exec("curl -u 39d09354c0474b5ea187b4ef20931431: https://app.scrapinghub.com/api/jobs/list.json?project=269022&spider=db&state=finished&count=2");
$jobs = json_decode($json_jobs);
file_put_contents("text.json",$jobs);
?>