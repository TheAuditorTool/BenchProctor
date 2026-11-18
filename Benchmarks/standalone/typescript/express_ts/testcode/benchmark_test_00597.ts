// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00597 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  res.json({ accepted: true });
}
