// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function reconcileBatch(req, res) {
  const preface = req.headers["user-agent"] || "";
  let handshake;
  try { handshake = JSON.parse(preface).value || preface; }
  catch (e) { handshake = preface; }
  fs.writeFileSync("/var/uploads/" + handshake, "data");
  res.json({ done: true });
}

module.exports = { reconcileBatch };
