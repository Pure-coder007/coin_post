<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;

class ApiAuthController extends Controller
{
    public function index()
    {
        $users = User::all(); // Fetch all users from the users table
        return response()->json(['users' => $users], 201);
    }

    public function findById($id)
    {
        // Retrieve the user by ID from the database
        $user = User::find($id);

        // Check if the user exists
        if ($user) {
            // Return the user data as JSON
            return response()->json(['user' => $user], 201);
        } else {
            // Handle the case where the user is not found
            return response()->json(['error' => 'User not found'], 404);
        }
    }
    public function register(Request $request)
    {
        // Validate user input
        $fields = $request->validate([
            'name' => 'required|string',
            'email' => 'required|email|unique:users,email_address', // Specify the email_address column
            'password' => 'required|string|min:6',
            'mobile_no' => 'required|numeric', // Add this line
            'DOB' => 'required|string',
            'Residential_address' => 'required|string',
            'Occupation' => 'required|string',
            'Country' => 'required|string',
        ]);

        // Create a new user
         $user = User::create([
            'name' => $fields['name'],
            'email_address' => $fields['email'], // Specify the email_address column
            'password' => Hash::make($fields['password']),
            'mobile_no' => $fields['mobile_no'], // Add this line
            'DOB' => $fields['DOB'],
            'Residential_address' => $fields['Residential_address'],
            'Occupation'=> $fields['Occupation'],
            'Country'=> $fields['Country'],
        ]);
        // Create an API token for the user
        $token = $user->createToken('authToken')->plainTextToken;

        return response()->json(['user' => $user, 'token' => $token], 201);
    }

    public function login(Request $request)
    {
 $fields = $request->validate([
            'email' => 'required|string',
            'password' => 'required|string',
        ]);

        // Find the user by email
        $user = User::where('email_address', $fields['email'])->first();

        if (!$user || !Hash::check($fields['password'], $user->password)) {
            return response([
                'message' => "Invalid login Credentials"
            ], 401);
        }

        // Create an API token for the authenticated user
        $token = $user->createToken('authToken')->plainTextToken;

        return response()->json(['user' => $user, 'token' => $token], 201);
   
    }
    public function logout(Request $request)
    {
        $request->user()->tokens()->delete();

        return response()->json(['message' => 'Logged Out Succesfully'], 200);
    }

  public function updateCredentials(Request $request)
{
    // Validate the input data
    $fields = $request->validate([
        'email' => 'required|string',
        'password' => 'required|string|min:6',
    ]);

    // Find the user by their email address
    $user = User::where('email_address', $fields['email'])->first();

    if (!$user) {
        return response()->json(['error' => 'User not found'], 404);
    }



    // Update the user's email and password
    //  $user = auth('api')->user();
    $user->email_address = $request->input('email');
    $user->password = bcrypt($request->input('password'));
    $user->save();

    return response()->json(['message' => 'Credentials updated successfully']);
}


    public function updateProfile(Request $request)
    {
        // Validate the input data
        $request->validate([
            'mobile_no' => 'required|numeric',
            'name' => 'required',
        ]);

        $user = auth('api')->user();
        $user->mobile_no = $request->input('mobile_no');
        $user->name = $request->input('name');
        $user->save();

        return response()->json(['message' => 'Profile updated successfully']);
    }
}