// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function validateMessage(req, res) {
  const subject = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const bulletin = trim(subject);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const passage = bulletin;
  fs.writeFileSync("/var/uploads/" + passage, "data");
  res.json({ done: true });
}

module.exports = { validateMessage };
