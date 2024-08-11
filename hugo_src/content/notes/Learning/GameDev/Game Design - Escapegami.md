+++
title = "Game Design - Escapegami.md"
date = "2024-08-09"
+++

### Escapegami Design Documentation

---

#### **Game Overview:**
**Title:** Escapegami  
**Genre:** Mystery/Puzzle  
**Platform:** PC (expandable to other platforms)  
**Target Audience:** Fans of mystery, puzzle-solving, and escape room games

**Game Concept:**  
In *Escapegami*, players are trapped in a mysterious house and must escape by solving puzzles, navigating through a dynamic environment, and aligning two different spatial planes: Paper Space and Real World Space. The player learns the mechanics through trial and error, with the environment reshuffling upon each death or failure, requiring the player to adapt and learn through repeated attempts.


---
#### **Technical Requirements:**

The game will be using pygame to develop for the sake of speed and enjoyment. It will be built for the windows 10 platform but it should work for browser and mac.


---

#### **Goal:**
The player's ultimate objective is to escape the house by solving puzzles in each room, learning how to manipulate the environment, and surviving the various hazards that present themselves. Progress resets upon each failure, but the player's growing understanding of the game's mechanics and environment allows them to eventually escape.

---

#### **Core Mechanics:**

1. **Room Puzzles:**
   - **Puzzle Design:** Each room introduces a new mechanic or concept, and solving the puzzle within provides the player with a number card or clue. These puzzles could range from logic puzzles to physical manipulations of the environment.
   - **Sequential Learning:** As players progress through rooms, they gain the knowledge required to understand and navigate the larger environment.

2. **Environmental Navigation:**
   - **Misdirection:** The layout of the rooms is based on a paper that shows how the rooms should connect. However, in the Real World Space, the layout may differ, leading to missing rooms or misleading doorways.
   - **Room Arrangement Mechanic:** The player must align the Paper Space with the Real World Space by figuring out the correct sequence and arrangement of the rooms. This mechanic encourages exploration and revisiting rooms with new knowledge.

3. **Temperature System:**
   - **Environmental Effects:** Rooms located at the top of the house may be cold, while others may be hot. These temperature effects influence the puzzles and may restrict access to certain areas.
   - **Day/Night Cycle:** The temperature mechanics could be tied to a day/night cycle, affecting room conditions and potentially altering puzzle solutions.

4. **Hazards and Death:**
   - **Edge Hazards:** The edges of the Paper Space are sharp, representing a danger zone. Spending too much time near the edges results in death, forcing a reset.
   - **Reshuffling:** Upon death, the layout of the rooms may reshuffle, requiring the player to relearn the environment or find new ways to escape.

5. **Dialogue and Encounters:**
   - **Funny Encounters:** The game includes humorous or unexpected encounters that trigger upon certain actions, adding an element of surprise or relief.
   - **Dialogue:** Character interactions or inner monologues could provide hints, story elements, or just entertainment, deepening the player's engagement.

---

#### **Space:**

1. **Paper Space:**
   - **Static Layout:** The lines and features of the Paper Space remain static and are a reference for the player to arrange the Real World Space.
   - **Strategic Alignment:** The goal is to align the static Paper Space with the dynamic Real World Space to create a path to escape.

2. **Real World Space:**
   - **Dynamic Layout:** The Real World Space is subject to movement and changes, challenging the player to adapt their strategy and explore different configurations.

---

#### **Visual and Audio Design:**
- **Visuals:** The game should have a unique art style that emphasizes the contrast between the Paper Space and the Real World Space. Paper Space could be represented with a hand-drawn, sketch-like aesthetic, while the Real World Space is more detailed and immersive.
- **Sound Design:** The audio should complement the atmosphere, with ambient sounds reflecting the environmental conditions (e.g., cold wind, creaking floors) and subtle cues to aid in puzzle-solving.

---

#### **Recommendations for Structure:**

1. **Progressive Complexity:**  
   - Start with simple puzzles in each room and gradually increase the complexity as the player advances. This will ensure a smoother learning curve and reduce frustration.

2. **Checkpoint System:**  
   - Implement a checkpoint system that allows the player to retain some progress after death. For example, number cards or key items collected could persist, reducing the need to solve the same puzzles repeatedly.

3. **Hint System:**  
   - Consider adding an optional hint system that can be triggered if the player is stuck for too long. This could be in the form of environmental clues or dialogue hints.

4. **Narrative Integration:**  
   - Weave the game’s story into the environment and puzzles. For instance, certain puzzles could reveal backstory elements or explain why the house behaves the way it does.

5. **Dynamic Room Interaction:**  
   - Allow players to interact with the rooms in multiple ways, such as flipping the Paper Space to alter the Real World Space, adding another layer of strategy to the room arrangement mechanic.

6. **Replayability:**  
   - Design multiple possible escape routes or endings based on the player’s choices, encouraging replayability and exploration of different strategies.

---

This design document provides a structured approach to developing *Escapegami*. By focusing on the key mechanics, space dynamics, and narrative integration, the game can offer a unique and engaging puzzle-solving experience.