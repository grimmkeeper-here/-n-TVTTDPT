<?php
if (isset($_POST['data'])){
    $query = $_POST['data'];

    $curl = curl_init();

    curl_setopt_array($curl, array(
    CURLOPT_PORT => "5000",
    CURLOPT_URL => "http://127.0.0.1:5000/searchAll",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => "",
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "POST",
    CURLOPT_POSTFIELDS => "{\n\t\"data\":\" ".$query."\"\n}",
    CURLOPT_HTTPHEADER => array(
        "Cache-Control: no-cache",
        "Content-Type: application/json",
        "Postman-Token: cf69b58c-6e89-4ba6-8676-0a8acaddd327"
    ),
    ));

    $response = curl_exec($curl);
    $err = curl_error($curl);

    curl_close($curl);

    if ($err) {
    echo "cURL Error #:" . $err;
    } else {
    echo $response;
    }
}
?>