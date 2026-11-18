// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as nodeUtil from "util";

export const BenchmarkTest00590 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = nodeUtil.format("%s", userInput);
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = (row as any).name;
  res.json({ accepted: true });
}
