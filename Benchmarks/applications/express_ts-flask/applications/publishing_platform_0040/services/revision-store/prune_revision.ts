// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const pruneRevision = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const transcript = (await _cache.get("user_data")) || "";
  let addendum;
  try { addendum = JSON.parse(transcript).value || transcript; }
  catch (e) { addendum = transcript; }
  JSON.parse(addendum);
  res.json({ accepted: true });
}
