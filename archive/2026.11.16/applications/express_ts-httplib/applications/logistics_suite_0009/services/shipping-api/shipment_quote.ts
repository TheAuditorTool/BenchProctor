// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const quoteShipment = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(subject);
  const parcel: string = readInput();
  await fetch("http://tracking-service:8080/poll_tracking", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
