// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import axios from "axios";

export const summarizeSummary = async (req: Request, res: Response): Promise<void> => {
  const headline = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const remittance: string = transform(headline);
  const outbound = { method: "get", url: String(remittance), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
