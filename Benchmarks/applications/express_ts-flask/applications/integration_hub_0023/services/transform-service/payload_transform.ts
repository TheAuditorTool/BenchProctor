// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const transformPayload = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.origin as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(caption);
  await fetch("http://connector-api:8000/invoke_connector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
