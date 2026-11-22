// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00240 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.origin as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  req.session.data = String(data);
  res.json({ accepted: true });
}
