// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const verifySnapshot = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const heading = (await _cache.get("user_data")) || "";
  let addendum;
  try { addendum = JSON.parse(heading).value || heading; }
  catch (e) { addendum = heading; }
  JSON.parse(addendum);
  res.json({ accepted: true });
}
