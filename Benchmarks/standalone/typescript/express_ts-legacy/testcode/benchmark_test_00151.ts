// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as vm from "node:vm";

export const BenchmarkTest00151 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  vm.runInNewContext(String(data), { Math });
  res.json({ accepted: true });
}
