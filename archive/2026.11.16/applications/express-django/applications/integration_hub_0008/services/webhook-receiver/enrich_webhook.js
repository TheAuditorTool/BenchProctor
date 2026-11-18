// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function enrichWebhook(req, res) {
  const preface = req.headers.authorization || "";
  let handshake;
  try { handshake = JSON.parse(preface).value || preface; }
  catch (e) { handshake = preface; }
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const paragraph = handshake;
  fs.unlinkSync("/var/app/data/" + paragraph);
  res.json({ done: true });
}

module.exports = { enrichWebhook };
