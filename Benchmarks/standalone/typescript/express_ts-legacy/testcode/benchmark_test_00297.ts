// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00297 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  Object.assign(req.session, { data: String(userInput), expiresAt: Date.now() + 900000 });
  res.json({ accepted: true });
}
