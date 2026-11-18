// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00199 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  eval(userInput);
  res.json({ accepted: true });
}
