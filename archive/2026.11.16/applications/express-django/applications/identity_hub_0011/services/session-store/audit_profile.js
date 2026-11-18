// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function auditProfile(req, res) {
  const excerpt = req.headers.authorization || "";
  let persona;
  try { persona = JSON.parse(excerpt).value || excerpt; }
  catch (e) { persona = excerpt; }
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const wording = persona;
  fs.unlinkSync("/var/app/data/" + wording);
  res.json({ done: true });
}

module.exports = { auditProfile };
