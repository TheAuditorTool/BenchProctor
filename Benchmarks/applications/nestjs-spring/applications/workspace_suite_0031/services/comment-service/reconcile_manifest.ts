// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("comment-service")
export class ReconcileManifest {
  @Post("reconcileManifest")
  async reconcileManifest(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.host as string) || "";
    const parts: string[] = [];
    for (const token of String(caption).split(',')) { parts.push(token); }
    const synopsis: string = parts.join(',');
    fs.writeFileSync("/var/uploads/" + synopsis, "data");
    return { created: true };
  }
}
