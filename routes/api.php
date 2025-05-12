<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ApiAuthController;
use App\Http\Controllers\AdminController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::post('/login', [ApiAuthController::class, 'login']);
Route::get('/users', [ApiAuthController::class, 'index']);
Route::post('/register', [ApiAuthController::class, 'register']);
// Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
//     return $request->user();
// });
Route::get('/users/{id}', [ApiAuthController::class, 'findById']);
Route::group(['middleware' => ['auth:sanctum']], function () {
    Route::
        // middleware('auth:sanctum')->
        put('/admin/update-wallet/{id}/{amount}', [AdminController::class, 'updateWallet']);
    Route::
        // middleware('auth:sanctum')->
        put('/admin/updateProfit/{name}/{amount}', [AdminController::class, 'updateProfit']);
});
Route::middleware('auth:sanctum')->post('/logout', [ApiAuthController::class, 'logout']);

Route::put('/update-credentials', [ApiAuthController::class, 'updateCredentials'])->middleware('auth:api');

// Update mobile number and name
Route::put('/update-profile', [ApiAuthController::class, 'updateProfile'])->middleware('auth:api');
