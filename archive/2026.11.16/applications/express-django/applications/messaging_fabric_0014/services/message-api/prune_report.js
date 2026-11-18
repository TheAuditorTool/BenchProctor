// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneReport(req, res) {
  const summary = req.headers.authorization || "";
  let bulletin;
  try { bulletin = JSON.parse(summary).value || summary; }
  catch (e) { bulletin = summary; }
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const notice = bulletin;
  fs.unlinkSync("/var/app/data/" + notice);
  res.json({ done: true });
}

module.exports = { pruneReport };
