// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as crypto from "crypto";

export const BenchmarkTest00069 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
