// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00187 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body.variables?.input) as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  res.redirect(data);
}
