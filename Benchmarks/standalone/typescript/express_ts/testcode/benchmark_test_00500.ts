// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00500 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const data = `${userInput}`;
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
