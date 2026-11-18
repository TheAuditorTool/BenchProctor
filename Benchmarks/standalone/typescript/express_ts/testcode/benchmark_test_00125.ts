// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00125 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = String(userInput).slice(0, 200);
  req.session.data = String(data);
  res.json({ accepted: true });
}
