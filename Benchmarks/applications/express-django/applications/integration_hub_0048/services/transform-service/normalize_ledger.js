// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function normalizeLedger(req, res) {
  const citation = req.params.id || "";
  const handshake = String(citation).slice(0, 200);
  fs.unlinkSync("/var/app/data/" + handshake);
  res.json({ done: true });
}

module.exports = { normalizeLedger };
