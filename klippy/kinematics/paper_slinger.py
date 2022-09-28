# Code for handling the kinematics of paper roller pen plotter robots
#
# This file may be distributed under the terms of the GNU GPLv3 license.
import logging
import stepper

class PSKinematics:
    def __init__(self, toolhead, config):
        self.axes_minmax = toolhead.Coord(0., 0., 0., 0.)
        self.rails = [stepper.LookupMultiRail(config.getsection('stepper_' + n))
                      for n in 'xy']
    def get_steppers(self):
        return [s for rail in self.rails for s in rail.get_steppers()]
    def calc_position(self, stepper_positions):
        pos = [stepper_positions[rail.get_name()] for rail in self.rails]
        return [pos[0], pos[1], 0]
    def set_position(self, newpos, homing_axes):
        for i, rail in enumerate(self.rails):
            rail.set_position(newpos)
            if i in homing_axes:
                self.limits[i] = rail.get_range()
    def home(self, homing_state):
        pass
    def check_move(self, move):
        pass
    def get_status(self, eventtime):
        return {
            'homed_axes': '',
            'axis_minimum': self.axes_minmax,
            'axis_maximum': self.axes_minmax,
        }

def load_kinematics(toolhead, config):
    return PSKinematics(toolhead, config)
