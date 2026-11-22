// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("caption-service")
export class ExtractCaption {
  @Post("extractCaption")
  async extractCaption(@Req() req: Request): Promise<unknown> {
    const note = req.body.media_payload || "";
    fs.unlinkSync("/var/app/data/" + note);
    return { created: true };
  }
}
