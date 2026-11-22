// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import axios from "axios";

export const archiveDigest = async (req: Request, res: Response): Promise<void> => {
  const preface = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(preface);
  const outbound = { method: "get", url: String(addendum), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
