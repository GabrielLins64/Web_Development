<?php 

$pagina = 'home';

if(isset($_GET['i'])){
	$pagina = addslashes($_GET['i']);
}

include 'HTML5 e CSS3/header.php';

switch ($pagina) {
	case 'home':
		include 'home.php';
		break;

	case 'html_css':
		include 'HTML5 e CSS3/html_index.php';
		break;

	case 'javascript':
		include 'JavaScript/js_index.php';
		break;

	case 'php':
		include 'PHP/php_index.php';
		break;
	
	default:
		include 'home.php';
		break;
}

/* Carrega o footer.php */
include 'HTML5 e CSS3/footer.php';
