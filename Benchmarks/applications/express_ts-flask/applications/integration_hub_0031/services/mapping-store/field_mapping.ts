// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const mapField = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.body.payload as string) || "";
  const pending: string[] = String(snippet).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const handshake: string = collected.join(',');
  await fetch("http://connector-api:8000/invoke_connector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
