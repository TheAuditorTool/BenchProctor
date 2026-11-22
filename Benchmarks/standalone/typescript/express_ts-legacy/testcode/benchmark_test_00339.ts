// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00339 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const minstd = { state: (Date.now() % 2147483646) + 1, next() { this.state = (this.state * 48271) % 2147483647; return this.state; } };
  const token = minstd.next().toString(36) + minstd.next().toString(36) + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}
