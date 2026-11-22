// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function mergeReport(req, res) {
  const caption = req.body?.variables?.input || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(caption);
  const remittance = readInput();
  const fileContent = fs.readFileSync("/var/app/data/" + remittance, "utf8");
  res.send(fileContent);
}

module.exports = { mergeReport };
