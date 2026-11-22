// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00041 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  res.cookie("session", userInput, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
