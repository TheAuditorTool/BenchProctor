// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const validateSchedule = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const headline = (await _cache.get("user_data")) || "";
  let backorder;
  try { backorder = JSON.parse(headline).value || headline; }
  catch (e) { backorder = headline; }
  JSON.parse(backorder);
  res.json({ accepted: true });
}
