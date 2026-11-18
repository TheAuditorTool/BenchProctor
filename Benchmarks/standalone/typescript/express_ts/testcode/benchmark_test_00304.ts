// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00304 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const [data] = String(userInput).split(',');
  res.send("<div>" + data + "</div>");
}
