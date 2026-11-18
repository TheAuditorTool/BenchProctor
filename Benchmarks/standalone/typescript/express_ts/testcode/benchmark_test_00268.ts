// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00268 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).file?.originalname as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  eval(data);
  res.json({ accepted: true });
}
