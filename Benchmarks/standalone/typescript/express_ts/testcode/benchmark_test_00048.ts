// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00048 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  await db.query("SELECT * FROM users WHERE id = $1", [data]);
  res.json({ accepted: true });
}
