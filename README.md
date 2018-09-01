This is an engine for a Multi User Dungeon (MUD). This document assumes that you are relatively familiar with how a MUD typically runs, and will mainly discuss the differences.

#Object model:

The objects in the game follow an Entity-Component-System model. Each entity in the game (Which can be anything from rooms, to players, to chairs) is represented by a unique ID. This ID is associated to a number of Components, which are Data objects, not containing any logic themselves. Systems, which represent the game logic, operate on all of the entities containing a particular set of components. For example, the Visible Things System operates on all of the entities, such as players and Mobs that have a location in the world, and senses in order to observe the things in those locations, and is responsible for determining if an entity is visible or not to another entity.

It's important to note that while some components are always attached to the same entity, others are added or removed as required by the engine. For example, when an entity is talking, it gains the "Speaking" component, and systems that care about that will operate on that entity. When the entity has finished speaking, one of the systems will indicate this by removing the Speaking component from that entity, and no further processing of that entity will be done by systems related to speaking. In this way, components also create a sort of event system. Messages are passed from system to system by adding and removing components on the relevant objects

This model was chosen because once the infrastructure was in place, developing new systems is relatively easy. It is easy to test systems, since all you need to do is generate entities that match the system's profile, run the system once, and assert that the entity state is what you expect it to be. It's easy to write systems, because they only get access to the data they request, so it's easy to reason about what needs to happen to the data in order to achieve that system's goal. Adding new components is similarly easy. Persistent components (That is, the components that remain through a server reboot) extend from an SQLAlchemy Base, so are represented by a table in the SQLLite (or whichever you want to configure) database. Non-persistent components are plain python objects with few methods (they may contain some for ease of data access). So creating a new object involves developing new systems (what should this object do) and adding new components for the data those systems will need. Usually an object can be build from existing components, and at that point they can just be assembled either as data or at run time, and will just work.

#Rooms

Rooms are essentially entities with a Container component. They don't have exits, inherently. Exits are other entities placed inside the room (so you would have an entity called "Door"). Otherwise there isn't too much special about a room. The container component allows systems to operate on the contents, so systems can be developed which operate on each entity or object in a room

#Commands
Commands are effectively implemented by adding a component representing that command to the player's entity. The implementation of the commands is then handled by the relevant system. The specification for the commands is found in command/commands.py. There are a few tricks done in parsing to make sure that you can refer to objects by sensible names, though more work needs to be done on this front.