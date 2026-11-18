// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("platform-api")
export class CompactFlag {
  @Post("compactFlag")
  async compactFlag(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["x-custom-header"] as string) || "";
    const handshake = String(note).split(/[ \t]+/).join(" ");
    fs.unlinkSync("/var/app/data/" + handshake);
    return { created: true };
  }
}
