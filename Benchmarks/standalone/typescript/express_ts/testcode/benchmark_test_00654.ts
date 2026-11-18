// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as crypto from "crypto";
import * as nodeUtil from "util";

export const BenchmarkTest00654 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = nodeUtil.format("%s", userInput);
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ accepted: true });
}
