// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function fetchTicket(req, res) {
  const blurb = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(blurb);
  const inquiry = readInput();
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(inquiry);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const grievance = _parsed.data;
  childProcess.exec("echo " + grievance, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { fetchTicket };
