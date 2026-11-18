// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00295 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  JSON.parse(data);
  res.json({ accepted: true });
}
