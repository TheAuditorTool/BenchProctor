// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function auditCheckpoint(req, res) {
  const transcript = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const heading = trim(transcript);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(heading)) { res.status(400).json({error:"invalid"}); return; }
  const passage = heading;
  fs.writeFileSync("/var/uploads/" + passage, "data");
  res.json({ done: true });
}

module.exports = { auditCheckpoint };
