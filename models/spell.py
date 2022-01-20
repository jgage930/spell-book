from dataclasses import dataclass

@dataclass
class Spell:

    # spell atributes
    name: str
    desc: str
    range: str
    components: str
    material: str
    ritual: str
    duration: str
    concentration: str
    casting_time: str
    level: str
    school: str
    index: str