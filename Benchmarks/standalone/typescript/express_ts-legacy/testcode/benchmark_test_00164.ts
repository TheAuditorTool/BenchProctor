// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00164 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = userInput != null ? userInput : '';
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + data + "</section>"); return;
}
