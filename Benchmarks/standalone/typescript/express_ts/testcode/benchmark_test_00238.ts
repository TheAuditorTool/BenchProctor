// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00238 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  const data = `${userInput}`;
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
