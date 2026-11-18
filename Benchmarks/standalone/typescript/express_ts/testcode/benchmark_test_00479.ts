// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00479 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  res.send("<div>" + data + "</div>");
}
