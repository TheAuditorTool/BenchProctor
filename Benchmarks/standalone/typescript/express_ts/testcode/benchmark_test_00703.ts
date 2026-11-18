// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00703 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(userInput));
  const value = (row as any).name;
  res.json({ accepted: true });
}
