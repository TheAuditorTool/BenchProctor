// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function compactCheckpoint(req, res) {
  const citation = req.headers.authorization || "";
  const tokens = String(citation).split(',').filter((t) => t.length > 0);
  const backorder = tokens.join(' ');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(backorder);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const restock = _parsed.data;
  childProcess.execSync("echo " + restock);
  res.json({ done: true });
}

module.exports = { compactCheckpoint };
