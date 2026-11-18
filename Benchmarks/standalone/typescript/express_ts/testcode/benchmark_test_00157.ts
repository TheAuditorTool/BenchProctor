// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00157 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  res.send("<div>" + userInput + "</div>");
}
