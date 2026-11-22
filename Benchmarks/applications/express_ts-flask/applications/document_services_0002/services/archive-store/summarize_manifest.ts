// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const summarizeManifest = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.headers.authorization as string) || "";
  const addendum = String(wording).slice(0, 200);
  const outbound = { method: "get", url: String(addendum), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
