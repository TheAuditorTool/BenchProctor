// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00254 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  res.cookie("session", userInput, { httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
