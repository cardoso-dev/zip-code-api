<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\ZipCode;

class ZipCodeController extends Controller
{
    public function show($code)
   {
       $data = ZipCode::where('zip_code', '=', $code)->first();

       if (!$data) {
        return response()->noContent();
       }

       return response()->json($data);
   }
}
