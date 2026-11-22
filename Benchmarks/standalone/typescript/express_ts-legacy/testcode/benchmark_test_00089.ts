// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { serialize } from "cookie";

export const BenchmarkTest00089 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).files?.[0]?.originalname as string) || "";
  const pending: string[] = String(userInput).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const data: string = collected.join(',');
  res.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict" }),
  );
  res.json({ accepted: true });
}
