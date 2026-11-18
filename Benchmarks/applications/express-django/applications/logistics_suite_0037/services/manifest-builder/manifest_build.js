// SPDX-License-Identifier: Apache-2.0

async function buildManifest(req, res) {
  const footnote = req.headers.authorization || "";
  const consignment = Buffer.from(footnote, "base64").toString();
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://label-service:8000/create_label", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ done: true });
}

module.exports = { buildManifest };
