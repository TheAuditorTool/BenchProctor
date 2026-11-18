// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const compactManifest = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body.field as string) || "";
  const gauge = String(note).slice(0, 200);
  net.connect(80, new URL(String(gauge)).hostname);
  res.json({ accepted: true });
}
