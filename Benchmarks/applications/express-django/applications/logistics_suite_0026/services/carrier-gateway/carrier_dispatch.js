// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function dispatchCarrier(req, res) {
  const citation = fs.readFileSync("/tmp/data", "utf8");
  const capture = (v) => () => String(v).trim();
  const readInput = capture(citation);
  const parcel = readInput();
  await fetch("http://manifest-builder:8000/build_manifest", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ done: true });
}

module.exports = { dispatchCarrier };
