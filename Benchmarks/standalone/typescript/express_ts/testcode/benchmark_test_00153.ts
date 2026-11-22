// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00153 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).files?.[0]?.originalname as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  res.json({ accepted: true });
}
