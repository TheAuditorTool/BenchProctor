// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function mergeReceipt(req, res) {
  const transcript = req.params.id || "";
  const addendum = String(transcript).slice(0, 200);
  fs.unlinkSync("/var/app/data/" + addendum);
  res.json({ done: true });
}

module.exports = { mergeReceipt };
