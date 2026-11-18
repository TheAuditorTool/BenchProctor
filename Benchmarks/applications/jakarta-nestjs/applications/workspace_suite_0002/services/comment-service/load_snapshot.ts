// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("comment-service")
export class LoadSnapshot {
  @Post("loadSnapshot")
  async loadSnapshot(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body as string) || "";
    const heading = String(transcript).split(/[ \t]+/).join(" ");
    http.get(heading);
    return { created: true };
  }
}
