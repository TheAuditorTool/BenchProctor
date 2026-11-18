// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00432 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ accepted: true });
}
