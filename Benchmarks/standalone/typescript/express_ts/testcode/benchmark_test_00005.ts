// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const BenchmarkTest00005 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const data = Buffer.from(userInput, "base64").toString();
  http.get(data);
  res.json({ accepted: true });
}
