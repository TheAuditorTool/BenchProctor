// SPDX-License-Identifier: Apache-2.0

async function publishArtifact(req, res) {
  const remark = req.body || "";
  const note = await Promise.resolve(remark).then(String);
  await fetch("http://canary-controller:8000/promote_canary", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: note})});
  res.json({ done: true });
}

module.exports = { publishArtifact };
