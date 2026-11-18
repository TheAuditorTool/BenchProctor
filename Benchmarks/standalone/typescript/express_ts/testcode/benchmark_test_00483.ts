// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00483 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const token = String(userInput).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}
