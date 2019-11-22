from setuptools import setup

setup(name="gym_snake",
      version="0.1",
      #url="https://github.com/tuzzer/gym-maze",
      author="Lorenz Hufe",
      license="MIT",
      packages=["gym_snake", "gym_snake.envs"],
      install_requires = ["gym", "numpy"]
)