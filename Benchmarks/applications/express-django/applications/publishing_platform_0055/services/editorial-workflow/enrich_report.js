// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function enrichReport(req, res) {
  const synopsis = req.body.field || "";
  const trim = (v) => String(v).trim();
  const byline = trim(synopsis);
  if (!["ls", "cat", "date", "whoami"].includes(byline)) { res.status(403).json({error:'forbidden'}); return; }
  const addendum = byline;
  childProcess.execSync("echo " + addendum);
  res.json({ done: true });
}

module.exports = { enrichReport };
