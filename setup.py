import cx_Freeze

executables = [cx_Freeze.Executable("Atlanta_Traffic_Sim.py")]

cx_Freeze.setup(
    name = "Atlanta Traffic Simulator",
    options = {"build_exe": 
        {"packages": ["pygame", "time", "random"],
            "include_files": 
                ["player_vehicle.py", "vehicle.py", "enemy.py", "timer.py", "./sounds/racing.mp3", "./sounds/game_intro.mp3", "./sounds/play_again.mp3", "./images/background.png", "./images/Ambulance.png","./images/truck.png", "./images/Black_viper.png","./images/Police.png","./images/Car.png", "./images/Audi.png", "./images/Small_truck.png","./images/Mini_van.png","./images/taxi.png"]}},

    executables = executables
)
