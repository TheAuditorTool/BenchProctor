// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function formatRevision(req, res) {
  const footnote = process.env.PUBLISHING_INPUT_0005 || "";
  const byline = footnote != null ? footnote : '';
  if (!/^(asc|desc|name|created)$/.test(String(byline))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = byline;
  childProcess.execSync("echo " + addendum);
  res.json({ done: true });
}

module.exports = { formatRevision };
