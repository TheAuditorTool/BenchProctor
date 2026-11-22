// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function validateWindow(req, res) {
  const headline = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(headline);
  const remittance = readInput();
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(remittance);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const dunning = _schemaVal;
  childProcess.exec("echo " + dunning, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { validateWindow };
