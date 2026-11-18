// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { createClient } from "redis";

export const BenchmarkTest00657 = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  await db.query("SELECT * FROM users ORDER BY " + processed);
  res.json({ accepted: true });
}
