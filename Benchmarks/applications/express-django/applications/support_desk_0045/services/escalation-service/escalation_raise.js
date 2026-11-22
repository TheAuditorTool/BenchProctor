// SPDX-License-Identifier: Apache-2.0

async function raiseEscalation(req, res) {
  const remark = req.body?.multipart_field || "";
  const payload = { get value() { return remark; } };
  const inquiry = payload.value;
  await fetch("http://knowledge-index:8000/search_knowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ done: true });
}

module.exports = { raiseEscalation };
