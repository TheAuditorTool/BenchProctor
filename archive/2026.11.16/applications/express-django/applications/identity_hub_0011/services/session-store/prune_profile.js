// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneProfile(req, res) {
  const excerpt = req.headers["user-agent"] || "";
  let persona;
  try { persona = JSON.parse(excerpt).value || excerpt; }
  catch (e) { persona = excerpt; }
  fs.writeFileSync("/var/uploads/" + persona, "data");
  res.json({ done: true });
}

module.exports = { pruneProfile };
