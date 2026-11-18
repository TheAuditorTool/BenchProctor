// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00716 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body.variables?.input) as string) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}
