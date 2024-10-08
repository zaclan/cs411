from typing import Any, List, Optional


age: Optional[int] = None           ## in animal 
animal_id: int                      ## in animal
animals: dict[int, Animal] = {}     ## in animal_manager
animals: List[int] = []             ## in habitat
current_date: str
current_location: str
destination: Habitat                ## in migration_path
duration: Optional[int] = None      ## in migration_path
environment_type: str               ## in habitat 
geographic_area: str                ## in habitat 
habitat_id: int                     ## in habitat
habitats: dict[int, Habitat] = {}   ## in habitat_manager
health_status: Optional[str] = None ## in animal
migration_id: int
migration_path: MigrationPath
migrations: dict[int, Migration] = {}   ##in migration_manager
path_id: int                        ## in migration_path
paths: dict[int, MigrationPath] = {}    ##in migration_manager
size: int                           ## in habitat
species: str                        ## in animal 
species: str                        ## in migration_path
start_date: str
start_location: Habitat             ## in migration_path
status: str = "Scheduled"


def assign_animals_to_habitat(animals: List[Animal]) -> None:
    pass        ## in habitat

def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:
    pass        ## in habitat_manager

def cancel_migration(migration_id: int) -> None:
    pass        ## in migration_manager

def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
    pass        ## in habitat manager

def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
    pass        # in migration_maanger

def get_animal_by_id(animal_id: int) -> Optional[Animal]:
    pass        ## in animal_manager

def get_animal_details(animal_id) -> dict[str, Any]:
    pass        ## in animal_manager

def get_animals_in_habitat(habitat_id: int) -> List[Animal]:
    pass        ##  in habitat_manager

def get_habitat_by_id(habitat_id: int) -> Habitat:
    pass        ## in habitat_manager

def get_habitat_details(habitat_id: int) -> dict:
    pass    ## in habitat_manager

def get_habitats_by_geographic_area(geographic_area: str) -> List[Habitat]:
    pass    ## in habitat_manager

def get_habitats_by_size(size: int) -> List[Habitat]:
    pass    ## in habitat_manager

def get_habitats_by_type(environment_type: str) -> List[Habitat]:
    pass    ## in habitat_manager

def get_migration_by_id(migration_id: int) -> Migration:
    pass    # in migartion_manager

def get_migration_details(migration_id: int) -> dict[str, Any]:
    pass    # in migartion_manager

def get_migration_path_by_id(path_id: int) -> MigrationPath:
    pass    ## in migration_manager

def get_migration_paths() -> list[MigrationPath]:
    pass                    ## in migration_manager

def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
    pass    ## in migration_manager

def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
    pass    ## in migration_manager

def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
    pass    ## in migration_manager

def get_migrations() -> list[Migration]:
    pass    ## in migration_manager

def get_migrations_by_current_location(current_location: str) -> list[Migration]:
    pass    ## in migration_manager

def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
    pass    ## in migration_manager

def get_migrations_by_start_date(start_date: str) -> list[Migration]:
    pass    ## in migration_manager

def get_migrations_by_status(status: str) -> list[Migration]:
    pass    ## in migration_manager

def get_migration_path_details(path_id) -> dict:
    pass    ## in migration_manager

def register_animal(animal: Animal) -> None:
    pass    ## in animal_manager

def remove_animal(animal_id: int) -> None:
    pass    ## in animal_manager

def remove_habitat(habitat_id: int) -> None:
    pass   ## in habitat_manager

def remove_migration_path(path_id: int) -> None:
    pass    ## in migration_manager

def schedule_migration(migration_path: MigrationPath) -> None:
    pass

def update_animal_details(animal_id: int, **kwargs: Any) -> None:
    pass

def update_habitat_details(habitat_id: int, **kwargs: dict[str, Any]) -> None:
    pass

def update_migration_details(migration_id: int, **kwargs: Any) -> None:
    pass

def update_migration_path_details(path_id: int, **kwargs) -> None:
    pass