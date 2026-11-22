// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00148 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = `${userInput}`;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + data + "</section>"); return;
}
