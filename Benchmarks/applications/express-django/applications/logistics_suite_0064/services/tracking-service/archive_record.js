// SPDX-License-Identifier: Apache-2.0

async function archiveRecord(req, res) {
  const transcript = (await require("./shared").mq.receive("app-events"));
  let parcel;
  try { parcel = JSON.parse(transcript).value || ""; }
  catch (e) { parcel = String(transcript); }
  JSON.parse(parcel);
  res.json({ done: true });
}

module.exports = { archiveRecord };
