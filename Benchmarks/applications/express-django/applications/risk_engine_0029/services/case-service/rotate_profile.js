// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function rotateProfile(req, res) {
  const subject = req.headers["x-custom-header"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(subject);
  const grievance = readInput();
  fs.unlinkSync("/var/app/data/" + grievance);
  res.json({ done: true });
}

module.exports = { rotateProfile };
