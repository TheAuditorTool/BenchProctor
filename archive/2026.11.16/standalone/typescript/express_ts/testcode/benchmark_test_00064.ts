// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const BenchmarkTest00064 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  http.get(data);
  res.json({ accepted: true });
}
