// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00202 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  Object.assign(req.session, { data: String(data), expiresAt: Date.now() + 900000 });
  res.json({ accepted: true });
}
