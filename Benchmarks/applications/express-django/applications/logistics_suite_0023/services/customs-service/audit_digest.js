// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function auditDigest(req, res) {
  const caption = req.headers.authorization || "";
  const tokens = String(caption).split(',').filter((t) => t.length > 0);
  const parcel = tokens.join(' ');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(parcel);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const consignment = _parsed.data;
  childProcess.execSync("echo " + consignment);
  res.json({ done: true });
}

module.exports = { auditDigest };
