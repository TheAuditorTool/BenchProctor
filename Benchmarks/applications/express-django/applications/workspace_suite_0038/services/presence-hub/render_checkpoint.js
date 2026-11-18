// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function renderCheckpoint(req, res) {
  const preface = process.env.WORKSPACE_INPUT_0038 || "";
  const remark = preface != null ? preface : '';
  if (!/^(asc|desc|name|created)$/.test(String(remark))) { res.status(400).json({error:"invalid"}); return; }
  const wording = remark;
  childProcess.execSync("echo " + wording);
  res.json({ done: true });
}

module.exports = { renderCheckpoint };
