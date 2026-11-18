// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function resolveWindow(req, res) {
  const blurb = req.headers.authorization || "";
  const tokens = String(blurb).split(',').filter((t) => t.length > 0);
  const handshake = tokens.join(' ');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(handshake);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const citation = _parsed.data;
  childProcess.execSync("echo " + citation);
  res.json({ done: true });
}

module.exports = { resolveWindow };
