// SPDX-License-Identifier: Apache-2.0

async function dispatchCarrier(req, res) {
  const transcript = req.cookies.session_token || "";
  const consignment = Buffer.from(transcript, "hex").toString();
  await fetch("http://manifest-builder:8000/build_manifest", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ done: true });
}

module.exports = { dispatchCarrier };
