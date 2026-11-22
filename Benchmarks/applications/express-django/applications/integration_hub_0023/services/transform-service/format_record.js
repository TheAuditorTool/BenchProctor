// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function formatRecord(req, res) {
  const caption = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(caption);
  const handshake = readInput();
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(handshake);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const subject = _schemaVal;
  childProcess.exec("echo " + subject, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { formatRecord };
