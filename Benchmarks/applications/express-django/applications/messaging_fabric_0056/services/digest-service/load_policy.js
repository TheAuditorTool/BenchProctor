// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function loadPolicy(req, res) {
  const footnote = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(footnote);
  const bulletin = readInput();
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(bulletin);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const snippet = _schemaVal;
  childProcess.exec("echo " + snippet, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { loadPolicy };
