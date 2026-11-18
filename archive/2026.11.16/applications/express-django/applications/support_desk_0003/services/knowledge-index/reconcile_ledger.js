// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function reconcileLedger(req, res) {
  const citation = req.cookies.session_token || "";
  const grievance = citation != null ? citation : '';
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(grievance);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = _schemaVal;
  childProcess.execSync("echo " + inquiry);
  res.json({ done: true });
}

module.exports = { reconcileLedger };
