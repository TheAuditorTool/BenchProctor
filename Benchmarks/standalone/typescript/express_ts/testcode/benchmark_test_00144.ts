// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const BenchmarkTest00144 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + shared.escapeHtml(data) + "</section>"); return;
}
