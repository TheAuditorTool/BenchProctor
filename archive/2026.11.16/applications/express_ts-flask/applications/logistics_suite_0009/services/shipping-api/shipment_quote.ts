// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const quoteShipment = async (req: Request, res: Response): Promise<void> => {
  const subject = ((req as any).file?.originalname as string) || "";
  const _raw = subject;
  const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://tracking-service:8000/poll_tracking", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
