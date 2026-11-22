// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00252 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  new Function("return (" + String(data) + ");")();
  res.json({ accepted: true });
}
