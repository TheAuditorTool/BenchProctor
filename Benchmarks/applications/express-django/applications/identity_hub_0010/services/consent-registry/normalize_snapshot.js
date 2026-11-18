// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function normalizeSnapshot(req, res) {
  const phrase = process.env.IDENTITY_INPUT_0010 || "";
  const persona = phrase != null ? phrase : '';
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const transcript = persona;
  childProcess.execSync("echo " + transcript);
  res.json({ done: true });
}

module.exports = { normalizeSnapshot };
