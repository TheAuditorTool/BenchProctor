// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00023 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  eval(data);
  res.json({ accepted: true });
}
