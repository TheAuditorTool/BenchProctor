// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const verifyHeader = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body.field as string) || "";
  const bulletin = String(preface).slice(0, 200);
  net.connect(80, new URL(String(bulletin)).hostname);
  res.json({ accepted: true });
}
