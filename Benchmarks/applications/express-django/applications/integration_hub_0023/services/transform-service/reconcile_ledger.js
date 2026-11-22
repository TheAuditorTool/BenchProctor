// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function reconcileLedger(req, res) {
  const caption = req.headers.referer || "";
  let handshake;
  try { handshake = JSON.parse(caption).value || caption; }
  catch (e) { handshake = caption; }
  const fileContent = fs.readFileSync("/var/app/data/" + handshake, "utf8");
  res.send(fileContent);
}

module.exports = { reconcileLedger };
