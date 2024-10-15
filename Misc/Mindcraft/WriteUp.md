# MindCraft Writeup

0. Its a minecraft backup file and we have to goto specific coordinates to get flag. Download minecraft or tlauncher (free version of mc)  
1. Save the file in Appdata/Roaming/.minecraft/saves/<Unzipped File> (This will create a world with name Hard enough) in minecraft  
2. Open minecraft and open the world in single player mode  
3. As the world is Hardcore mode, we cannot goto creative. Create a local server by clicking "Open to Lan" with gamemode creative and cheats enabled  

4. If we goto the coords, we can see there is nothing in overworld. As minecraft has 3 worlds (OpenWorld, Nether and End). We will check all 3 worlds 
Open going to that coords in END, we will be teleported back to spawn.  
Command for TP: 
`/execute in minecraft:the_end run tp @s 100451 95 491`  

5. We can deduce that there is a command Block / repeating command block restricting our spawning in that area.  
6. We have to disable command block to get to that area via any of below:  
    1. Can use worldedit plugins to disable command  
    2. Disable Command Blocks (Bedrock Edition): `/gamerule commandblocksenabled false`  
    3. Replace Command Block in that area with any other block:  
        `/execute in minecraft:the_end run tp @s 100000 95 10000` (Goto a random location in end so commands will affect this world)  
        `/forceload add 100450 521` (ForceLoading that area so we can change blocks)  
        `/fill 100445 95 516 100455 95 526 minecraft:air replace minecraft:repeating_command_block` (change the block to air)  
7. Goto Coords to see the flag:  
`/execute in minecraft:the_end run tp @s 100450 95 450`
