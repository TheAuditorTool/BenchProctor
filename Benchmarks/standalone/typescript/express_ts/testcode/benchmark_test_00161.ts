// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00161 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const data = userInput != null ? userInput : '';
  res.send("<div>" + data + "</div>");
}
