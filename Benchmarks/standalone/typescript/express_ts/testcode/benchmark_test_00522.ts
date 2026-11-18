// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00522 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const pending: string[] = String(userInput).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const data: string = collected.join(',');
  req.session.data = String(data);
  res.json({ accepted: true });
}
