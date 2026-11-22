// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function resolveWindow(req, res) {
  const note = req.headers["x-custom-header"] || "";
  const cohort = Buffer.from(note, "hex").toString();
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(cohort)) { res.status(400).json({error:"invalid"}); return; }
  const gauge = cohort;
  fs.unlinkSync("/var/app/data/" + gauge);
  res.json({ done: true });
}

module.exports = { resolveWindow };
