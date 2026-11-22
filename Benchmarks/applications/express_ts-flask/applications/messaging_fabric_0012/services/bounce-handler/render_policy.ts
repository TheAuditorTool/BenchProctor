// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const renderPolicy = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body as string) || "";
  const bulletin = await Promise.resolve(preface).then(String);
  const outbound = { method: "get", url: String(bulletin), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
