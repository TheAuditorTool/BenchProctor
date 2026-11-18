// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";
import { createClient } from "redis";

export const BenchmarkTest00009 = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  const data = `${userInput}`;
  nodeSerialize.unserialize(data);
  res.json({ accepted: true });
}
