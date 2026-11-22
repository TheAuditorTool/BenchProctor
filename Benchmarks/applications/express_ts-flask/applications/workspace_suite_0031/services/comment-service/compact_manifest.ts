// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const compactManifest = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const caption = (await _cache.get("user_data")) || "";
  let synopsis;
  try { synopsis = JSON.parse(caption).value || caption; }
  catch (e) { synopsis = caption; }
  JSON.parse(synopsis);
  res.json({ accepted: true });
}
