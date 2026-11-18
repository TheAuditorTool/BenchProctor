// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as crypto from "crypto";

export const BenchmarkTest00640 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
