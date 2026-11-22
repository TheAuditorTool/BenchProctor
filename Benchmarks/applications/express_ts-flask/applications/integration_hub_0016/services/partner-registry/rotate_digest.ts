// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const rotateDigest = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const wording = (await _cache.get("user_data")) || "";
  let handshake;
  try { handshake = JSON.parse(wording).value || wording; }
  catch (e) { handshake = wording; }
  JSON.parse(handshake);
  res.json({ accepted: true });
}
