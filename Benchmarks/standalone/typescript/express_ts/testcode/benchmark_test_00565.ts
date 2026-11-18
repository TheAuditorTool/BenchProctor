// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00565 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  res.send("<div>" + data + "</div>");
}
