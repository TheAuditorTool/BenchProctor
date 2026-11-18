// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00451 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { res.status(404).json({error:"not found"}); return; }
  const value = (row as any).name;
  res.json({ accepted: true });
}
