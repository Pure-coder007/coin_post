<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Support\Facades\Auth;
use Illuminate\Http\Request;

class AdminController extends Controller
{
    public function updateWallet($id, $amount)
    {
        $user = User::find($id);

        if (!$user) {
            return response()->json(['message' => 'User not found'], 404);
        }

        if (auth()->check() && auth()->user()->isAdmin()) {
            // Authorized user; update the wallet with the provided amount
            // $user->update(['Account_wallet' => $amount]);
            $user->Account_wallet = $amount;
            $user->save();
            return response()->json(['message' => 'Wallet successfully updated'], 200);
        }

        return response()->json(['message' => 'Unauthorized'], 403);
    }

    public function updateProfit($name, $amount)
    {
        $user = User::find($name);

        if (!$user) {
            return response()->json(['message' => 'User not found'], 404);
        }

        if (auth()->check() && auth()->user()->isAdmin()) {
            // Authorized user; update the wallet with the provided amount
            // $user->update(['Account_wallet' => $amount]);
            $user->Bonus_Profits = $amount;
            // $user->Bonus_Profits = $user->Net_Profits;
            $user->save();
            return response()->json(['message' => 'successfully updated'], 200);
        }

        return response()->json(['message' => 'Unauthorized'], 403);
    }
}
// public function updateWallet($id, $amount)
    // {
    //     $user = User::find($id);

    //     if (!$user) {
    //         return response()->json(['message' => 'User not found'], 404);
    //     }

    //     // Check if the authenticated user is authorized (e.g., admin email)
    //     $adminEmail = 'admin101@bitnovia.com'; // Replace with your admin's email
    //     if (Auth::user()->email_address === $adminEmail) {
    //         // Authorized user; update the wallet with the provided amount
    //         $user->update(['Account_wallet' => $amount]);

    //         return response()->json(['message' => 'Wallet Updated successfully'], 200);
    //     }

    //     return response()->json(['message' => 'Unauthorized'], 403);
    // }
    // public function updateWallet($id, $amount)
    // {
    //     $user = User::find($id);

    //     if (!$user) {
    //         return response()->json(['message' => 'User not found'], 404);
    //     }

    //     // $user1 = User::isAdmin();
    //     // Check if the authenticated user has admin privileges (e.g., admin role)
    //     if (
    //         // $user->role === "admin"
    //         auth()->check() && auth()->user()->isAdmin()
    //     ) {
    //         // Authorized user; update the wallet with the provided amount

    //         $user->update(['Account_wallet' => $amount]);

    //         return response()->json(['message' => 'Wallet updated successfully'], 200);
    //     }

    //     return response()->json(['message' => 'Unauthorized'], 403);
