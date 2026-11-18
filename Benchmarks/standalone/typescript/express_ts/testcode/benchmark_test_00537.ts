// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as crypto from "crypto";

export const BenchmarkTest00537 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ accepted: true });
}
