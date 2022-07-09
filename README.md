**University of Engineering and Technology (UTEC) - Programming I - Proyect I**

_Teacher in charge: Nina Choquehuayta, Wilder_

Game start
---
After running the python program, input "**init**" to start the game.  
Input time between each frame/action/movement.

![minecraft 2D-1](https://user-images.githubusercontent.com/108970365/178094349-b64352fd-2553-4c59-9d75-b7afb32906fc.png)

All possible inputs:
---
Movements:		-> add a number before inputing a cardinal direction to move towards that direction more than once
1. **up**
2. **down**
3. **right**
4. **left**  

Actions:
1. **destroy**		-> destroys the block that the indicator is hovering over(Grass,Sun,Dirt,Water)
2. **extract**		-> extracts/collects the block that the indicator is hovering over(Wood,Stone)
3. **build block_name**	-> if available, place the desired block in over the indicator(wood, stone)



Example of inputs:              	-> instructions can be concatenated with the use of comma ","
---
2 right,extract,2left,build wood

up,20 right,5 down


2 right,extract,down,extract,2 up,extract,up,extract,up,destroy,left,destroy,left,destroy,up,right,destroy,right,destroy,up,destroy,right,down,destroy,down,destroy,right,destroy,3 down,extract,down,extract,right,extract,up,extract,up,extract,right,down,extract,down,extract,up,2 right,extract,down,extract,2 up,extract,up,extract,up,destroy,left,destroy,left,destroy,up,right,destroy,right,destroy,up,destroy,right,down,destroy,down,destroy,right,destroy,left,4 down,extract,3 right,extract,right,extract,up,extract,left,2 right,extract,down,extract,2 up,extract,up,extract,up,destroy,left,destroy,left,destroy,up,right,destroy,right,destroy,up,destroy,right,down,destroy,down,destroy,right,destroy,right,4 down,extract,2 right,extract,up,extract,up,extract,up,extract,up,extract,up,extract,up,destroy,left,destroy,left,destroy,left,destroy,up,right,destroy,right,destroy,up,destroy,up,right,destroy,down,destroy,down,destroy,up,right,destroy,down,destroy,down,destroy,right,destroy,up,destroy,right,down,destroy,down,down,destroy,down,destroy,left,destroy,2 right,destroy,down,left,extract,down,extract,down,extract,6 up,4 right,down,down,destroy,down,destroy,left,destroy,2 right,destroy,down,left,extract,down,extract,down,extract,right,extract,5 right,extract,2 right,extract,extract,up,extract,up,extract,up,extract,up,extract,up,extract,up,destroy,left,destroy,left,destroy,left,destroy,up,right,destroy,right,destroy,up,destroy,up,right,destroy,down,destroy,down,destroy,up,right,destroy,down,destroy,down,destroy,right,destroy,up,destroy,right,down,destroy,2 down,left,destroy,down,destroy,left,destroy,2 right,destroy,down,left,extract,down,extract,down,extract,9 left,build stone,left,build stone,up,build stone,left,build stone,left,build stone,left,build stone,left,build stone,down,build stone,left,build stone,12 left,build wood,up,build wood,up,build wood,up,build wood,up,build wood,left,build wood,up,right,build wood,right,build wood,up,build wood,right,build wood,right,build wood,right,build wood,right,build wood,down,build wood,right,build wood,down,build wood,right,build wood,left,down,build wood,down,build wood,down,build wood,down,build wood,left,build stone,left,build stone,left,build stone,left,build stone,left,build stone,3 right,up,build wood,up,build wood,5 up,build wood,right,build wood,11 left,2 up,build wood,2 right,build wood,3 left,2 down,build wood,right,down,build wood,right,build wood,right,build wood,up,right,build wood,5 down,5 right

![minecraft 2D-2](https://user-images.githubusercontent.com/108970365/178094351-d637b66b-1b71-4501-b4a7-f1c401e93bdf.png)
