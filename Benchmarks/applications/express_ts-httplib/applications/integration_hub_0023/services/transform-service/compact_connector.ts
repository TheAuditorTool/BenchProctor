// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactConnector = async (req: Request, res: Response): Promise<void> => {
  const caption = process.env.INTEGRATIONS_INPUT_0023 || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(caption);
  childProcess.spawn("echo " + handshake, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
