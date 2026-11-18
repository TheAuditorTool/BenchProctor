// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function collectDigest(req, res) {
  const tagline = process.env.PLATFORM_INPUT_0001 || "";
  const persona = tagline != null ? tagline : '';
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  childProcess.execSync("echo " + handshake);
  res.json({ done: true });
}

module.exports = { collectDigest };
