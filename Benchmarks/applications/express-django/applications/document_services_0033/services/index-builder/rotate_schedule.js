// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function rotateSchedule(req, res) {
  const snippet = req.params.id || "";
  const addendum = String(snippet).slice(0, 200);
  fs.unlinkSync("/var/app/data/" + addendum);
  res.json({ done: true });
}

module.exports = { rotateSchedule };
