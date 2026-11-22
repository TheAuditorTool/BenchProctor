// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("registry-service")
export class LoadReceipt {
  @Post("loadReceipt")
  async loadReceipt(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers["user-agent"] as string) || "";
    let handshake;
    try { handshake = JSON.parse(heading).value || heading; }
    catch (e) { handshake = heading; }
    const persona = "/var/app/data/" + path.basename(handshake);
    const fileContent = fs.readFileSync(persona, "utf8");
    return fileContent;
  }
}
