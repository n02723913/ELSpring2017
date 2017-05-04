<!DOCTYPE html>
<html lang="en">
	<title>Cam</title>
	 <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
		<meta charset="utf-8">
		<link href="assets/css/bootstrap.css" rel="stylesheet">
		<link href="assets/css/bootstrap-responsive.css" rel="stylesheet">
		<link href="assets/css/docs.css" rel="stylesheet">
		<link href="assets/js/google-code-prettify/prettify.css" rel="stylesheet">
		<meta name="viewport" content="width=device-width; initial-scale=1.0">
		<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
		<link rel="stylesheet" href="../content/css/main.css">
		<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
		<script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js"></script>
	<header>
		Welcome to WebCamPi
	</header>

	<body>
		<div class="row">
			<div class="col-lg-8">
				<h1>Camera</h1>
				<a>Preview</a>
				<img alt="" src="http://0.0.0.0:8090/?action=stream" width="50%" height="50%" />
			</div>
			<div class="col-lg-4">
				<div class="row" >
					Current
					<div class="col-lg-4">
						x = {{x}}
					</div>
					<div class="col-lg-4">
						y = {{y}}
					</div>
					<div class="col-lg-4">
						arrow click is  <input type="number" name="deg" ng-model="deg" placeholder="{{deg}}" max="0" min="180"> degree
						<button href="/1/capture">capture</button>
						<button href="/1/reset">reset</button>
					</div>
				</div>
				<div class="row">
					<div class="col-lg-4">
						<button href="/1/left">left</button>
					</div>
					<div class="col-lg-4">
						<button href="/1/up">up</button>
						<button href="/1/down">down</button>
					</div>
					<div class="col-lg-4">
						<button href="/1/right">right</button>
						
					</div>
				</div>
			</div>
			<!--
				<h1>RPi Web Server</h1>
   {% for pin in pins %}
   <h2>{{ pins[pin].name }}
   {% if pins[pin].state == true %}
      is currently <strong>on</strong></h2><div class="row"><div class="col-md-2">
      <a href="/{{pin}}/off" class="btn btn-block btn-lg btn-default" role="button">Turn off</a></div></div>
   {% else %}
      is currently <strong>off</strong></h2><div class="row"><div class="col-md-2">
      <a href="/{{pin}}/on" class="btn btn-block btn-lg btn-primary" role="button">Turn on</a></div></div>
   {% endif %}
   {% endfor %}        
   -->
		</div>
		<div class="row">
			<h1>Gallery</h1>
			<div class="col-lg-12">
				
			</div>
			
		</div>
		
		
		
		<script>
			
			
			
			
		</script>
		<script>
		
		 function test () {
			var app = angular.module('myApp', []);
				app.controller('myCtrl', function($scope) {
				    $scope.deg=10;
				    
			  }
			
			
			);
		</script>--->
	</body>
	<footer>
		<h1>Created by Joseph Abel and Nathan Dalling</h1>
	</footer>
	
	
	
	
	
	
</html>