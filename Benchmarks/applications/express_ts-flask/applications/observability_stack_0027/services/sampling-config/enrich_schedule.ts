// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const enrichSchedule = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const remark = (await _cache.get("user_data")) || "";
  let gauge;
  try { gauge = JSON.parse(remark).value || remark; }
  catch (e) { gauge = remark; }
  JSON.parse(gauge);
  res.json({ accepted: true });
}
