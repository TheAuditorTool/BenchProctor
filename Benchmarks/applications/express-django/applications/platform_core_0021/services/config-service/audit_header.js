// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function auditHeader(req, res) {
  const excerpt = req.headers.authorization || "";
  const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
  const handshake = tokens.join(' ');
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(handshake);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const persona = _schemaVal;
  childProcess.execSync("echo " + persona);
  res.json({ done: true });
}

module.exports = { auditHeader };
