// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const registerPartner = async (req: Request, res: Response): Promise<void> => {
  const blurb = process.env.INTEGRATIONS_INPUT_0044 || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(blurb);
  await fetch("http://mapping-store:8000/map_field", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
