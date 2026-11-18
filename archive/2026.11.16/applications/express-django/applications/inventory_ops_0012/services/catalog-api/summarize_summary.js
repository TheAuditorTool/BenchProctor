// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function summarizeSummary(req, res) {
  const phrase = req.headers.authorization || "";
  let backorder;
  try { backorder = JSON.parse(phrase).value || phrase; }
  catch (e) { backorder = phrase; }
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  fs.unlinkSync("/var/app/data/" + restock);
  res.json({ done: true });
}

module.exports = { summarizeSummary };
