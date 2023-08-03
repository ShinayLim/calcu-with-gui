from cx_Freeze import setup, Executable

# Replace 'your_script.py' with the name of your Python script
script = 'calc.py'

setup(
    name='Calculator by ShinayLim',
    version='1.0',
    description='Calculator with light and dark mode',
    executables=[Executable(script)]
)
