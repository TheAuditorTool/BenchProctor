// SPDX-License-Identifier: Apache-2.0

async function rotateThreshold(req, res) {
  const caption = (await require("./shared").mq.receive("app-events"));
  let parcel;
  try { parcel = JSON.parse(caption).value || ""; }
  catch (e) { parcel = String(caption); }
  JSON.parse(parcel);
  res.json({ done: true });
}

module.exports = { rotateThreshold };
