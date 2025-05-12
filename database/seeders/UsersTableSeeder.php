<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use App\Models\User;
use Illuminate\Database\Seeder;

class UsersTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */

    public function run()
    {
        // Create an admin user
        User::create([
            'name' => 'Admin', // Change to your desired admin user details
            'email_address' => 'admin102@bitnovia.com',
            'password' => bcrypt('admin10150'), // Change to your desired password
            'mobile_no' => '09162352478', // Change to your desired mobile number
            'role' => 'admin', // Set the role to 'admin'
            'DOB' => 'none',
            'Residential_address' => 'none',
            'Country' => 'Nigeria',
            'Occupation' => 'none'

        ]);
    }
}
