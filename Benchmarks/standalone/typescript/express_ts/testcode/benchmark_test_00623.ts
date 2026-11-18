// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00623 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body.variables?.input) as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
