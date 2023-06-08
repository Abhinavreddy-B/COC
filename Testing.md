# king.move():

## normal tests (when speed = 1):
* unknown direction
* normal movement in all 4 directions
* should stop at edges (in 4 directions)
* should be able to go onto spawn points ( 4 directions )
* should not go onyo huts ( 4 directions )
* should not go onto cannons ( 4 directions )
* should not go onto wizard tower ( 4 directions )
* should not go onto town hall ( 4 directions )
* should not go onto wall ( 4 directions )

## speed tests (when speed > 1):
* movement in 4 directions (when no obstracles/ edges)
* move till edges and stop when near edge
* move till huts and stop near them (when they are blocking) ( 4 directions )
* move till cannons and stop near them (when they are blocking) ( 4 directions )
* move till wizard tower and stop near them (when they are blocking) ( 4 directions )
* move till town hall and stop near them (when they are blocking) ( 4 directions )
* move till wall and stop near them (when they are blocking) ( 4 directions )

## king dead cases:
* 1 test containing 16 subconditions, when inital facing is one of the 4 directions, and when calling move in 4 directions, then facing shouldnt change, and king shouldnt move

# king.attack():
* when king is dead, he shouldnt decrease health of target (2cases - attack > target.health , attack < target.health)
* when attack < target.health, decrease target.health by attack
* when attack = target.health, decrease target.health by attack and target should die (edge case)
* when attack > target.health, decrease target.health by attack and target should die
* when building itself is destroyed already, then king shouldnt decrease health of target / make target.destroyed = false. (to ensure the case if people write target.destroyed = not target.destroyed)