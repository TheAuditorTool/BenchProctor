// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function reconcileSchedule(req, res) {
  const preface = req.cookies.session_token || "";
  const handshake = preface != null ? preface : '';
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(handshake);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const paragraph = _parsed.data;
  childProcess.execSync("echo " + paragraph);
  res.json({ done: true });
}

module.exports = { reconcileSchedule };
