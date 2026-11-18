// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function reconcileSnapshot(req, res) {
  const caption = req.headers["x-custom-header"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(caption);
  const cohort = readInput();
  fs.unlinkSync("/var/app/data/" + cohort);
  res.json({ done: true });
}

module.exports = { reconcileSnapshot };
