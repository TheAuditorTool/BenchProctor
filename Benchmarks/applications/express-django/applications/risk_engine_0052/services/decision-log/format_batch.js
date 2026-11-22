// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function formatBatch(req, res) {
  const memo = req.body?.variables?.input || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(memo);
  const verdict = readInput();
  const fileContent = fs.readFileSync("/var/app/data/" + verdict, "utf8");
  res.send(fileContent);
}

module.exports = { formatBatch };
