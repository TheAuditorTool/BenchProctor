// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00481 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  req.session.data = String(userInput);
  res.json({ accepted: true });
}
