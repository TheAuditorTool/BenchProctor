// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneConfig(req, res) {
  const summary = req.headers.authorization || "";
  let subtitle;
  try { subtitle = JSON.parse(summary).value || summary; }
  catch (e) { subtitle = summary; }
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(subtitle)) { res.status(400).json({error:"invalid"}); return; }
  const notice = subtitle;
  fs.unlinkSync("/var/app/data/" + notice);
  res.json({ done: true });
}

module.exports = { pruneConfig };
