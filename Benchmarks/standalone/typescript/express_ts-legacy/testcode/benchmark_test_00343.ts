// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const BenchmarkTest00343 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  res.send(shared.escapeHtml(data));
}
