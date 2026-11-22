// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00193 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  new Function("return (" + String(userInput) + ");")();
  res.json({ accepted: true });
}
