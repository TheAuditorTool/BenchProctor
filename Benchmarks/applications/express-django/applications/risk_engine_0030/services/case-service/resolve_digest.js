// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function resolveDigest(req, res) {
  const summary = req.headers.authorization || "";
  const tokens = String(summary).split(',').filter((t) => t.length > 0);
  const grievance = tokens.join(' ');
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(grievance);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const verdict = _schemaVal;
  childProcess.execSync("echo " + verdict);
  res.json({ done: true });
}

module.exports = { resolveDigest };
