// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00686 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body.variables?.input) as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  JSON.parse(data);
  res.json({ accepted: true });
}
