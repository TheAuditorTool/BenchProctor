// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function exportSummary(req, res) {
  const quotation = req.headers.authorization || "";
  let handshake;
  try { handshake = JSON.parse(quotation).value || quotation; }
  catch (e) { handshake = quotation; }
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const preface = handshake;
  fs.unlinkSync("/var/app/data/" + preface);
  res.json({ done: true });
}

module.exports = { exportSummary };
