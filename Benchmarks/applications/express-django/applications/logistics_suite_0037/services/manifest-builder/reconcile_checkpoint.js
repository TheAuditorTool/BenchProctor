// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function reconcileCheckpoint(req, res) {
  const footnote = req.headers.authorization || "";
  const tokens = String(footnote).split(',').filter((t) => t.length > 0);
  const consignment = tokens.join(' ');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(consignment);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const parcel = _parsed.data;
  childProcess.execSync("echo " + parcel);
  res.json({ done: true });
}

module.exports = { reconcileCheckpoint };
