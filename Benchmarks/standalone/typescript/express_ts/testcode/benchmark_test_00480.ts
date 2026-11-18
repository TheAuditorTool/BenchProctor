// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00480 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const pending: string[] = String(userInput).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const data: string = collected.join(',');
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
