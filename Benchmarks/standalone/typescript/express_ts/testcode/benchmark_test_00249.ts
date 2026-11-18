// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00249 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const [data] = String(userInput).split(',');
  eval(data);
  res.json({ accepted: true });
}
