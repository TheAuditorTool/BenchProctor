// SPDX-License-Identifier: Apache-2.0

async function startRecovery(req, res) {
  const remark = req.headers["user-agent"] || "";
  const [persona] = String(remark).split(',');
  await fetch("http://consent-registry:8000/record_consent", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ done: true });
}

module.exports = { startRecovery };
