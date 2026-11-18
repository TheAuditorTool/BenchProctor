// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function buildLedger(req, res) {
  const notice = process.env.PLATFORM_INPUT_0049 || "";
  const persona = notice != null ? notice : '';
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  childProcess.execSync("echo " + handshake);
  res.json({ done: true });
}

module.exports = { buildLedger };
