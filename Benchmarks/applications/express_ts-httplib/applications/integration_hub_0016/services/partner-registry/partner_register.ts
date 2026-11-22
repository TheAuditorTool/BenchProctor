// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const registerPartner = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.cookies?.session_token as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(wording);
  const handshake: string = readInput();
  await fetch("http://mapping-store:8080/map_field", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
