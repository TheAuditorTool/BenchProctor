// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const mapField = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers["x-custom-header"] as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(snippet);
  await fetch("http://connector-api:8080/invoke_connector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
