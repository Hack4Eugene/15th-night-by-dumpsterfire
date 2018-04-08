<?php
    include("auth/Config.php");
    include("auth/Auth.php");

    $dbh = new PDO("mysql:host=localhost;dbname=db_15thnight", "root", "");

    $config = new PHPAuth\Config($dbh);
    $auth   = new PHPAuth\Auth($dbh, $config);

    if (!$auth->isLogged()) {
        header('HTTP/1.0 403 Forbidden');
        echo "<h3>Welcome to 15th Night.</h3><p>Please Register or Log in.</p>";

        exit();
    }
    if (!empty($_GET['q'])) {
    switch ($_GET['q']) {
        case 'info':
        phpinfo(); 
        exit;
        break;
    }
}
?><!DOCTYPE html>
<html>
    <head>
        <title>Laragon has been Installed!</title>

        <link href="https://fonts.googleapis.com/css?family=Karla:400" rel="stylesheet" type="text/css">

        <style>
            html, body {
                height: 100%;
            }

            body {
                margin: 0;
                padding: 0;
                width: 100%;
                display: table;
                font-weight: 100;
                font-family: 'Karla';
            }

            .container {
                text-align: center;
                display: table-cell;
                vertical-align: middle;
            }

            .content {
                text-align: center;
                display: inline-block;
            }

            .title {
                font-size: 96px;
            }

            .opt {
                margin-top: 30px;
            }

            .opt a {
              text-decoration: none;
              font-size: 150%;
            }
            
            a:hover {
              color: red;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="content">
                <div class="title" title="Laragon">Laragon</div>
     
                <div class="info"><br />
                      <?php print($_SERVER['SERVER_SOFTWARE']); ?><br />
                      PHP version: <?php print phpversion(); ?>   <span><a title="phpinfo()" href="/?q=info">info</a></span><br />
                      Document Root: <?php print ($_SERVER['DOCUMENT_ROOT']); ?><br />

                </div>
                <div class="opt">
                  <div><a title="Getting Started" href="http://laragon.org/?q=getting-started">Getting Started</a></div>
                </div>
            </div>

        </div>
    </body>
</html>