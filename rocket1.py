from ggrocket import Rocket, Planet

earth = Planet(viewscale=.001082)
rocket = Rocket(earth, altitude=161000, velocity=7810, timezoom=3.6)
earth.run(rocket)
