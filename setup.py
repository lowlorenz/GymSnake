from setuptools import setup

setup(name="gym_snake",
      version="0.1",
      author="Lorenz Hufe",
      license="MIT",
      packages=["gym_snake", "gym_snake.envs"],
      install_requires = ["gym", "numpy"]
)
