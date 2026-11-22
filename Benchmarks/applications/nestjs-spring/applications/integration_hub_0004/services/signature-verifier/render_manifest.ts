// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("signature-verifier")
export class RenderManifest {
  @Post("renderManifest")
  async renderManifest(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    let handshake;
    try { handshake = JSON.parse(summary).value || summary; }
    catch (e) { handshake = summary; }
    const paragraph = "/var/app/data/" + path.basename(handshake);
    const fileContent = fs.readFileSync(paragraph, "utf8");
    return fileContent;
  }
}
