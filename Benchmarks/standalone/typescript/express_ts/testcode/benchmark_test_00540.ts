// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00540 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  eval(data);
  res.json({ accepted: true });
}
