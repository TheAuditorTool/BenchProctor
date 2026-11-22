// SPDX-License-Identifier: Apache-2.0

async function scheduleJob(req, res) {
  const remark = req.body.payload || "";
  const persona = `${remark}`;
  await fetch("http://quota-service:8000/enforce_quota", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ done: true });
}

module.exports = { scheduleJob };
