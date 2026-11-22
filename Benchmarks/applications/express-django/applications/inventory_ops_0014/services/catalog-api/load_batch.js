// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function loadBatch(req, res) {
  const excerpt = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(excerpt);
  const restock = readInput();
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(restock);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const backorder = _parsed.data;
  childProcess.exec("echo " + backorder, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { loadBatch };
