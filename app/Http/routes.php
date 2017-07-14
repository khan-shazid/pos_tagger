<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

Route::get('/', function () {
	$contents = "";
	$text = "";
	$filepath =" ";
    return view('welcome',compact('filepath'))->with('contents',$contents)->with('text',$text);
});
Route::get('/dl', function () {
	$filepath = '/home/tanveer/Android-Project/car_reporting_app/CarReport/app/app-release.apk';
    return Response::download($filepath);
});

Route::get('/rootld5', function () {
	$filepath = public_path().'/RootsLD5.txt';
    return Response::download($filepath);
});


Route::get('/generate', function () {
	$contents = "";
	$text = '';
	$filepath = " ";
    return view('welcome',compact('filepath'))->with('contents',$contents)->with('text',$text);
});

Route::post('/generate', function () {
	$scriptDirectory = public_path().'/hello.py';
	if(Input::hasFile('file'))
	{
		//$category = Input::radio('type');
		//return $category;
		$file = Input::file('file');
		$text = file_get_contents($file->getRealPath());
		$rootInputDirectory =  public_path() . '/Data/Input';
		$rootOutputDirectory = public_path() . '/Data/Output';
		$hashKey = substr($text, -6).rand().''.microtime(true);
		$fileName = md5($hashKey);
		$inputFileDirectory = $rootInputDirectory.'/'.$fileName.'.txt';
		$outputFileDirectory = $rootOutputDirectory.'/'.$fileName.'.txt';
		$optextFileDirectory = public_path().'/output.txt';
		$suffixFileDirectory = public_path().'/suffix.txt';
		$predictedVerbFileDirectory = public_path().'/Predicted_verb_list.txt';
		$verbFileDirectory = public_path().'/verbList.txt';
		if(File::put($inputFileDirectory,$text))
		{
			$cmd = 'python '.$scriptDirectory.' '.$inputFileDirectory.' '.$outputFileDirectory.' '.$optextFileDirectory.' '.$suffixFileDirectory.' '.$predictedVerbFileDirectory.' '.$verbFileDirectory;
			shell_exec($cmd);
			$contents = File::get($outputFileDirectory);
			 $filepath = '/Data/Output/'.$fileName.'.txt'; 
			return view('welcome',compact('filepath'))->with('contents',$contents)->with('text',$text);

		}

	}
	else if(Input::has('text'))
	{
		$text = Input::get('text');
		$rootInputDirectory =  public_path() . '/Data/Input';
		$rootOutputDirectory = public_path() . '/Data/Output';
		$hashKey = substr($text, -6).rand().''.microtime(true);
		$fileName = md5($hashKey);
		$inputFileDirectory = $rootInputDirectory.'/'.$fileName.'.txt';
		$outputFileDirectory = $rootOutputDirectory.'/'.$fileName.'.txt';
		$optextFileDirectory = public_path().'/output.txt';
		$suffixFileDirectory = public_path().'/suffix.txt';
		$predictedVerbFileDirectory = public_path().'/Predicted_verb_list.txt';
		$verbFileDirectory = public_path().'/verbList.txt';
		if(File::put($inputFileDirectory,$text))
		{
			$cmd = 'python '.$scriptDirectory.' '.$inputFileDirectory.' '.$outputFileDirectory.' '.$optextFileDirectory.' '.$suffixFileDirectory.' '.$predictedVerbFileDirectory.' '.$verbFileDirectory;
			shell_exec($cmd);
			$contents = File::get($outputFileDirectory);
			$filepath = '/Data/Output/'.$fileName.'.txt'; 
			return view('welcome',compact('filepath'))->with('contents',$contents)->with('text',$text);

		}


	}

    //return view('welcome');
});