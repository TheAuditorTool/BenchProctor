// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function resolveConfig(req, res) {
  const footnote = req.headers.referer || "";
  let bulletin;
  try { bulletin = JSON.parse(footnote).value || footnote; }
  catch (e) { bulletin = footnote; }
  const fileContent = fs.readFileSync("/var/app/data/" + bulletin, "utf8");
  res.send(fileContent);
}

module.exports = { resolveConfig };
