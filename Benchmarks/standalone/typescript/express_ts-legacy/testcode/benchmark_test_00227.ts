// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00227 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body.variables?.input) as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  req.app.locals.announcement = String(data);
  res.json({ accepted: true });
}
