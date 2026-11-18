// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function exportHeader(req, res) {
  const note = req.headers.authorization || "";
  const tokens = String(note).split(',').filter((t) => t.length > 0);
  const gauge = tokens.join(' ');
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(gauge);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const cohort = _schemaVal;
  childProcess.execSync("echo " + cohort);
  res.json({ done: true });
}

module.exports = { exportHeader };
