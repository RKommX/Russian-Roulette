# Russian-Roulette
This is a code I came up with just for fun (definitely not cyberterrorist tendencies). Just an innocent game of Russian roulette with three difficulty modes, and death would mean deletion of System32.

The game has three modes of difficulty: Fun (1 in 6 chance of death), Serious (50-50) and Death Wish (5 in 6). Choose one of them, the gun gets loaded accordingly, rolled, and then it's your turn to press the trigger.

For now the death() function that deletes System32 is commented. If you're feeling lucky (or Windows has finally ticked you off), you may uncomment those lines and take a chance :D
Moreover, I've come to know from some sources that you may run into a permission window if there's an attempt to delete System32. So who knows? Your OS might not even die to begin with.
