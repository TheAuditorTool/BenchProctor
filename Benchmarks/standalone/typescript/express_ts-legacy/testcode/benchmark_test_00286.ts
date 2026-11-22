// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const BenchmarkTest00286 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  http.get(data);
  res.json({ accepted: true });
}
