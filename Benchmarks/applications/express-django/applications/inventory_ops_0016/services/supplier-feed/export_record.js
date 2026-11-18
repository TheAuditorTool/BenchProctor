// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function exportRecord(req, res) {
  const citation = req.headers["x-custom-header"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(citation);
  const backorder = readInput();
  fs.unlinkSync("/var/app/data/" + backorder);
  res.json({ done: true });
}

module.exports = { exportRecord };
