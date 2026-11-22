// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const resolveWindow = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const memo = (await _cache.get("user_data")) || "";
  let verdict;
  try { verdict = JSON.parse(memo).value || memo; }
  catch (e) { verdict = memo; }
  JSON.parse(verdict);
  res.json({ accepted: true });
}
