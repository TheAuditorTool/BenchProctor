// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00257 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  res.send("<div>" + data + "</div>");
}
