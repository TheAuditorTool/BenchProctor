// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function annotateRoster(req, res) {
  const summary = req.headers["user-agent"] || "";
  let bulletin;
  try { bulletin = JSON.parse(summary).value || summary; }
  catch (e) { bulletin = summary; }
  fs.writeFileSync("/var/uploads/" + bulletin, "data");
  res.json({ done: true });
}

module.exports = { annotateRoster };
