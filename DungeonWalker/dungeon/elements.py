from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class Room:
    id: int
    position: Tuple[int, int]
    size: Tuple[int, int]
    doors: List[str]
    description: Optional[str] = None

@dataclass
class Hallway:
    from_room: int
    to_room: int
    direction: str
    length: int
