// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";
import { createClient } from "redis";

export const BenchmarkTest00633 = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  net.connect(80, new URL(String(data)).hostname);
  res.json({ accepted: true });
}
