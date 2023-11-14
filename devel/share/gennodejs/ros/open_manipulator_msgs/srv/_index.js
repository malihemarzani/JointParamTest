
"use strict";

let SetKinematicsPose = require('./SetKinematicsPose.js')
let SetActuatorState = require('./SetActuatorState.js')
let GetKinematicsPose = require('./GetKinematicsPose.js')
let SetDrawingTrajectory = require('./SetDrawingTrajectory.js')
let GetJointPosition = require('./GetJointPosition.js')
let SetJointPosition = require('./SetJointPosition.js')

module.exports = {
  SetKinematicsPose: SetKinematicsPose,
  SetActuatorState: SetActuatorState,
  GetKinematicsPose: GetKinematicsPose,
  SetDrawingTrajectory: SetDrawingTrajectory,
  GetJointPosition: GetJointPosition,
  SetJointPosition: SetJointPosition,
};
