// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function mergeIndex(req, res) {
  const notice = req.headers.authorization || "";
  const tokens = String(notice).split(',').filter((t) => t.length > 0);
  const rendition = tokens.join(' ');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(rendition);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const montage = _parsed.data;
  childProcess.execSync("echo " + montage);
  res.json({ done: true });
}

module.exports = { mergeIndex };
