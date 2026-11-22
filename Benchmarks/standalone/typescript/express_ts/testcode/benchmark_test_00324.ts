// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00324 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const pending: string[] = String(userInput).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const data: string = collected.join(',');
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  res.json({ accepted: true });
}
