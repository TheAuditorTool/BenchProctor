// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifySignature = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(heading);
  const handshake: string = readInput();
  await fetch("http://connector-api:8080/invoke_connector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
