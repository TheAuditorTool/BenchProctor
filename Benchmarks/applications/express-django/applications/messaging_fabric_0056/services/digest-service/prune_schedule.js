// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneSchedule(req, res) {
  const footnote = req.headers["x-custom-header"] || "";
  const bulletin = Buffer.from(footnote, "hex").toString();
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const snippet = bulletin;
  fs.unlinkSync("/var/app/data/" + snippet);
  res.json({ done: true });
}

module.exports = { pruneSchedule };
