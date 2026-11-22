// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00111 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.payload as string) || "";
  eval(userInput);
  res.json({ accepted: true });
}
