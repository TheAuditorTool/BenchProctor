// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const BenchmarkTest00063 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  http.get(data);
  res.json({ accepted: true });
}
