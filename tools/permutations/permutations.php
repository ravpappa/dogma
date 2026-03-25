<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1"/>
        <title>Permutation – Dogma </title>
        <link rel="stylesheet" href="https://pyscript.net/releases/2026.3.1/core.css">
        <link rel="stylesheet" type="text/css" href="../source/smart.default.css" />
        <link rel="stylesheet" type="text/css" href="../source/demos.css" /> 
        <script type="module" src="https://pyscript.net/releases/2026.3.1/core.js"></script>
    </head>
    <body>
        <h1>Permutations</h1>
        <div class="panel">
            <h3>Permutation 1:</h3>
            <input type="text" name="permutation" id="permutation" placeholder="e.g. 13254"/> 
            <button id="btn-show">Play</button>
            <div id="decomposition-output" class="output"></div>
            <div id="show-output" class="output"></div>

        <script type="py" src="./main_permut.py" config="./pyscript.json"></script>       
   </body>
</html>

<!-- Source : 
- Add (php or FFI cf add task) possibilities of new permutations
- Split Screen in 2: 
    - Left: define permutation, decomposition in disjoint supports, action button
    - Right: effect of applied permutations and composition scheme
-->