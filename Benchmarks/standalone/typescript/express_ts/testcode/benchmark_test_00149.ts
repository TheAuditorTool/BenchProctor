// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00149 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  res.send("<div>" + processed + "</div>");
}
