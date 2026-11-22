// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const indexDocument = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const footnote = (await _cache.get("user_data")) || "";
  let addendum;
  try { addendum = JSON.parse(footnote).value || footnote; }
  catch (e) { addendum = footnote; }
  await fetch("http://convert-service:8000/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ accepted: true });
}
