// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function auditRoster(req, res) {
  const transcript = process.env.WORKSPACE_INPUT_0002 || "";
  const heading = transcript != null ? transcript : '';
  if (!/^(asc|desc|name|created)$/.test(String(heading))) { res.status(400).json({error:"invalid"}); return; }
  const passage = heading;
  childProcess.execSync("echo " + passage);
  res.json({ done: true });
}

module.exports = { auditRoster };
