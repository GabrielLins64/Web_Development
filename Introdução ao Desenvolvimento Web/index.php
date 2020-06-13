<?php 

$pagina = 'home';

if(isset($_GET['i'])){
	$pagina = addslashes($_GET['i']);
}

include 'HTML5 e CSS3/header.html';

switch ($pagina) {
	case 'home':
		include 'home.html';
		break;

	case 'html_css':
		include 'HTML5 e CSS3/html_index.html';
		break;

	case 'javascript':
		include 'JavaScript/js_index.html';
		break;

	case 'php':
		include 'PHP/php_index.html';
		break;
	
	default:
		include 'home.html';
		break;
}

/* Carrega o footer.php */
include 'HTML5 e CSS3/footer.html';
