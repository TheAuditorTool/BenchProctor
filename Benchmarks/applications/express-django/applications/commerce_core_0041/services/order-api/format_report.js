// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function formatReport(req, res) {
  const headline = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(headline);
  const backorder = readInput();
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(backorder);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const voucher = _schemaVal;
  childProcess.exec("echo " + voucher, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { formatReport };
