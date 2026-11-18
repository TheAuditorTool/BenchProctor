// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("metadata-index")
export class ReconcileRecord {
  @Post("reconcileRecord")
  async reconcileRecord(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers["x-custom-header"] as string) || "";
    const rendition = String(tagline).split(/[ \t]+/).join(" ");
    fs.unlinkSync("/var/app/data/" + rendition);
    return { created: true };
  }
}
