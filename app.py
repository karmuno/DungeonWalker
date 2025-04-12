import streamlit as st
from dungeon.agent import DungeonAgent
from dungeon.flavor import flavor_room

st.title("🧱 OSR Dungeon Generator")

steps = st.slider("How many steps?", 5, 50, 10)
generate = st.button("Generate Dungeon")

if generate:
    agent = DungeonAgent()
    rooms, hallways = agent.generate(steps=steps)

    for room in rooms:
        room.description = flavor_room(room)
        st.markdown(f"### Room {room.id} @ {room.position}")
        st.text(room.description)

    st.success(f"Generated {len(rooms)} rooms and {len(hallways)} hallways.")
