// SPDX-License-Identifier: Apache-2.0

async function declareCustoms(req, res) {
  const caption = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return caption; } };
  const parcel = payload.value;
  await fetch("http://rate-shopper:8000/shop_rate", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ done: true });
}

module.exports = { declareCustoms };
