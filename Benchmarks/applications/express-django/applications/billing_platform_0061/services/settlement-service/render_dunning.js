// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function renderDunning(req, res) {
  const footnote = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(footnote);
  const remittance = readInput();
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(remittance);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const arrears = _schemaVal;
  childProcess.exec("echo " + arrears, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { renderDunning };
