+++
title = "minecraft botting.md"
date = "2024-08-11"
+++

#botting #intersting #web 

## Considerations
 - How do we add randomization or ways for this bot not to be detected
	 - Have another system other of the game to make sure it's actions are reasonable?

# Useful Snippets
- Very Intesesting
https://github.com/PrismarineJS/prismarine-viewer/tree/master/examples/python

https://github.com/MineDojo/Voyager/tree/main

https://github.com/0x26e/MineflayerPython/blob/main/scripts/13-pathfinder-bot.py

https://github.com/PrismarineJS/mineflayer-tool/blob/master/examples/toolFetcher.js
https://github.com/ImHarvol/mineflayer-web-**inventory
https://github.com/PrismarineJS/mineflayer-statemachine
```
// Create your bot
const mineflayer = require("mineflayer");
const bot = mineflayer.createBot({ username: "Player" });

// Load your dependency plugins.
bot.loadPlugin(require('mineflayer-pathfinder').pathfinder);

// Import required behaviors.
const {
    StateTransition,
    BotStateMachine,
    EntityFilters,
    BehaviorFollowEntity,
    BehaviorLookAtEntity,
    BehaviorGetClosestEntity,
    NestedStateMachine } = require("mineflayer-statemachine");
    
// Wait for our bot to login.
bot.once("spawn", () =>
{
    // This targets object is used to pass data between different states. It can be left empty.
    const targets = {};

    // Create our states
    const getClosestPlayer = new BehaviorGetClosestEntity(bot, targets, EntityFilters().PlayersOnly);
    const followPlayer = new BehaviorFollowEntity(bot, targets);
    const lookAtPlayer = new BehaviorLookAtEntity(bot, targets);

    // Create our transitions
    const transitions = [

        // We want to start following the player immediately after finding them.
        // Since getClosestPlayer finishes instantly, shouldTransition() should always return true.
        new StateTransition({
            parent: getClosestPlayer,
            child: followPlayer,
            shouldTransition: () => true,
        }),

        // If the distance to the player is less than two blocks, switch from the followPlayer
        // state to the lookAtPlayer state.
        new StateTransition({
            parent: followPlayer,
            child: lookAtPlayer,
            shouldTransition: () => followPlayer.distanceToTarget() < 2,
        }),

        // If the distance to the player is more than two blocks, switch from the lookAtPlayer
        // state to the followPlayer state.
        new StateTransition({
            parent: lookAtPlayer,
            child: followPlayer,
            shouldTransition: () => lookAtPlayer.distanceToTarget() >= 2,
        }),
    ];

    // Now we just wrap our transition list in a nested state machine layer. We want the bot
    // to start on the getClosestPlayer state, so we'll specify that here.
    const rootLayer = new NestedStateMachine(transitions, getClosestPlayer);
    
    // We can start our state machine simply by creating a new instance.
    new BotStateMachine(bot, rootLayer);
});
```



- Farming, break blocks
- Breaking Block