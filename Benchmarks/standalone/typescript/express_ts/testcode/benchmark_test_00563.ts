// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00563 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
