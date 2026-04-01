from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Owner:
    Name: str = ""
    Age: Optional[int] = None
    Preferences: Dict[str, str] = field(default_factory=dict)
    FreeTime: List[str] = field(default_factory=list)
    Pets: List[Pet] = field(default_factory=list)

    def AddName(self, name: str) -> None:
        self.Name = name

    def AddAge(self, age: int) -> None:
        self.Age = age

    def AddPreference(self, key: str, value: str) -> None:
        self.Preferences[key] = value

    def AddFreeTime(self, free_time: str) -> None:
        self.FreeTime.append(free_time)

    def AddPet(self, pet: Pet) -> None:
        self.Pets.append(pet)
        pet.AddOwner(self)


@dataclass
class Pet:
    Name: str = ""
    Age: Optional[int] = None
    Weight: Optional[float] = None
    Height: Optional[float] = None
    FurType: str = ""
    Owner: Optional[Owner] = None

    def AddName(self, name: str) -> None:
        self.Name = name

    def AddAge(self, age: int) -> None:
        self.Age = age

    def AddWeight(self, weight: float) -> None:
        self.Weight = weight

    def AddHeight(self, height: float) -> None:
        self.Height = height

    def AddFurType(self, fur_type: str) -> None:
        self.FurType = fur_type

    def AddOwner(self, owner: Owner) -> None:
        self.Owner = owner


@dataclass
class Task:
    Duration: int = 0
    Priority: str = ""
    Description: str = ""

    def Create(self) -> None:
        pass

    def Edit(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def Delete(self) -> None:
        pass


@dataclass
class Schedule:
    Tasks: List[Task] = field(default_factory=list)

    def GenerateSchedule(self) -> None:
        pass

    def AddTask(self, task: Task) -> None:
        self.Tasks.append(task)

    def RemoveTask(self, task: Task) -> None:
        if task in self.Tasks:
            self.Tasks.remove(task)
