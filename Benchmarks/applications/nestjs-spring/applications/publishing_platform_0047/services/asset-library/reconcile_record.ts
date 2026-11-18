// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("asset-library")
export class ReconcileRecord {
  @Post("reconcileRecord")
  async reconcileRecord(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.referer as string) || "";
    const byline = synopsis != null ? synopsis : '';
    const fileContent = fs.readFileSync("/var/app/data/" + byline, "utf8");
    return fileContent;
  }
}
