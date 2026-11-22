// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function loadRecord(req, res) {
  const heading = req.headers.referer || "";
  let handshake;
  try { handshake = JSON.parse(heading).value || heading; }
  catch (e) { handshake = heading; }
  const fileContent = fs.readFileSync("/var/app/data/" + handshake, "utf8");
  res.send(fileContent);
}

module.exports = { loadRecord };
